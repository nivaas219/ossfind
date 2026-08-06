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