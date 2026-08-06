import sys


def show_banner():
    print("=" * 40)
    print("OSSFind - Open Source Finder")
    print("=" * 40)


def main():
    show_banner()

    if len(sys.argv) < 2:
        print("Usage:")
        print("  ossfind search <keyword>")
        print("  ossfind login")
        print("  ossfind trending")
        return

    command = sys.argv[1]

    if command == "login":
        print("GitHub login feature coming soon.")

    elif command == "search":
        if len(sys.argv) < 3:
            print("Please provide a search keyword.")
            return

        keyword = sys.argv[2]
        print(f"Searching open source projects for: {keyword}")

    elif command == "trending":
        print("Trending repositories feature coming soon.")

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()