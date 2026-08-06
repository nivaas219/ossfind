import sys

from auth import github_login
from github_api import (
    search_repositories,
    get_user,
    get_authenticated_user,
    get_trending_repositories
)
from token_storage import load_token
 
def show_banner():
    print("=" * 40)
    print("OSSFind - Open Source Finder")
    print("=" * 40)


def main():

    show_banner()

    if len(sys.argv) < 2:
        print("Usage:")
        print("  ossfind login")
        print("  ossfind search <keyword>")
        print("  ossfind user <username>")
        print("  ossfind whoami")
        print("  ossfind trending")
        return


    command = sys.argv[1]


    if command == "login":

        token = github_login()

        if token:
            print("Login completed successfully")
        else:
            print("Login failed")


    elif command == "search":

        if len(sys.argv) < 3:
            print("Please provide keyword")
            return

        keyword = sys.argv[2]

        repos = search_repositories(keyword)

        for index, repo in enumerate(repos, start=1):

            print(f"{index}. {repo['full_name']}")
            print("⭐ Stars:", repo["stargazers_count"])
            print("Language:", repo["language"])
            print("Description:", repo["description"])
            print("URL:", repo["html_url"])
            print("-" * 50)


    elif command == "user":

        if len(sys.argv) < 3:
            print("Provide username")
            return

        username = sys.argv[2]

        user = get_user(username)

        if user:
            print("Name:", user["name"])
            print("Followers:", user["followers"])
        else:
            print("User not found")


    elif command == "whoami":

        token = load_token()

        if not token:
            print("Please login first")
            return

        user = get_authenticated_user(token)

        if user:
            print("Name:", user["name"])
            print("Username:", user["login"])
            print("Followers:", user["followers"])
            print("Profile:", user["html_url"])
        else:
            print("Unable to fetch user")


    elif command == "trending":

        repos = get_trending_repositories()

        print("\n🔥 Trending Open Source Projects\n")

        for index, repo in enumerate(repos, start=1):

            print(f"{index}. {repo['full_name']}")
            print("⭐ Stars:", repo["stargazers_count"])
            print("Language:", repo["language"])
            print("URL:", repo["html_url"])
            print("-" * 50)

    else:

        print("Unknown command:", command)



if __name__ == "__main__":
    main()
