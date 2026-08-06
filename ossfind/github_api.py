import requests

GITHUB_API = "https://api.github.com"


def get_user(username):
    url = f"{GITHUB_API}/users/{username}"

    response = requests.get(url)

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

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()["items"]

    return []
def get_authenticated_user(token):

    url = f"{GITHUB_API}/user"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        url,
        headers=headers
    )

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

    response = requests.get(
        url,
        params=params
    )

    if response.status_code != 200:
        return []

    data = response.json()

    return data.get("items", [])