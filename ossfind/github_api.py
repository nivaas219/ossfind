from datetime import datetime

import requests

GITHUB_API = "https://api.github.com"


class GitHubAPIError(Exception):
    """Base class for GitHub API failures the caller should react to."""


class AuthenticationError(GitHubAPIError):
    """The provided token was rejected (invalid, expired, or revoked)."""


class RateLimitError(GitHubAPIError):
    """The GitHub API rate limit has been exhausted."""


class NetworkError(GitHubAPIError):
    """The request could not reach the GitHub API."""


def _request(url, headers=None, params=None):
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
    except requests.exceptions.Timeout:
        raise NetworkError(
            "Request to GitHub timed out. Check your connection and try again."
        )
    except requests.exceptions.ConnectionError:
        raise NetworkError(
            "Could not reach GitHub. Check your internet connection."
        )
    except requests.exceptions.RequestException as error:
        raise NetworkError(f"Request to GitHub failed: {error}")

    if response.status_code == 401:
        raise AuthenticationError(
            "GitHub rejected the token — it may be invalid or expired. Try logging in again."
        )

    if response.status_code == 403 and response.headers.get("X-RateLimit-Remaining") == "0":
        reset_header = response.headers.get("X-RateLimit-Reset")
        reset_note = ""
        if reset_header:
            reset_time = datetime.fromtimestamp(int(reset_header)).strftime("%H:%M:%S")
            reset_note = f" Try again after {reset_time}."
        raise RateLimitError(f"GitHub API rate limit exceeded.{reset_note}")

    return response


def get_user(username):
    response = _request(f"{GITHUB_API}/users/{username}")

    if response.status_code == 200:
        return response.json()

    return None


def search_repositories(keyword):
    url = f"{GITHUB_API}/search/repositories"

    params = {
        "q": keyword,
        "sort": "stars",
        "order": "desc",
        "per_page": 10
    }

    response = _request(url, params=params)

    if response.status_code == 200:
        return response.json()["items"]

    return []


def get_authenticated_user(token):
    url = f"{GITHUB_API}/user"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = _request(url, headers=headers)

    if response.status_code == 200:
        return response.json()

    return None


def get_trending_repositories():
    url = f"{GITHUB_API}/search/repositories"

    params = {
        "q": "stars:>10000",
        "sort": "stars",
        "order": "desc",
        "per_page": 10
    }

    response = _request(url, params=params)

    if response.status_code != 200:
        return []

    data = response.json()

    return data.get("items", [])
