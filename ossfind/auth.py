import webbrowser
import requests
from token_storage import save_token
from urllib.parse import urlencode

from config import CLIENT_ID, CLIENT_SECRET


GITHUB_AUTHORIZE_URL = "https://github.com/login/oauth/authorize"
GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"


def github_login():
    print("Opening GitHub login...")

    params = {
        "client_id": CLIENT_ID,
        "scope": "repo user"
    }

    url = GITHUB_AUTHORIZE_URL + "?" + urlencode(params)

    webbrowser.open(url)

    print("\nAfter authorization, paste the code here:")
    code = input("Code: ")

    token = get_access_token(code)

    if token:
        save_token(token)
        print(" GitHub login successful")
        return token

    print(" Login failed")
    return None


def get_access_token(code):
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code
    }

    headers = {
        "Accept": "application/json"
    }

    response = requests.post(
        GITHUB_TOKEN_URL,
        data=data,
        headers=headers
    )

    result = response.json()

    return result.get("access_token")