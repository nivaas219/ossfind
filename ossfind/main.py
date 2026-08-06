import sys
from auth import github_login
from github_api import search_repositories, get_user


def show_banner():
    print("=" * 40)
    print("OSSFind - Open Source Finder")
    print("=" * 40)


def main():
    show_banner()

    if len(sys.argv) < 2:
        print("Usage:")
        print("  ossfind search <keyword>")
        print("  ossfind user <username>")
        return


    command = sys.argv[1]

    if command == "login":

        token = github_login()

        if token:
            print("Login completed successfully")
        else:
            print("Login failed")


    if command == "search":

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

        username = sys.argv[2]

        user = get_user(username)

        if user:
            print("Name:", user["name"])
            print("Followers:", user["followers"])
        else:
            print("User not found")


if __name__ == "__main__":
    main()