import os
import json

TOKEN_FILE = ".github_token.json"


def save_token(token):
    data = {
        "access_token": token
    }

    with open(TOKEN_FILE, "w") as file:
        json.dump(data, file)


def load_token():
    if not os.path.exists(TOKEN_FILE):
        return None

    with open(TOKEN_FILE, "r") as file:
        data = json.load(file)

    return data.get("access_token")


def delete_token():
    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)