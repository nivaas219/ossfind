#!/usr/bin/env python3
"""ossfind - Find open source contribution opportunities and swag programs."""

import argparse
from ossfind.github_api import find_issues
from ossfind.swag import list_swag

def main():
    parser = argparse.ArgumentParser(
        description="🔍 Find open source contribution opportunities and swag programs"
    )
    subparsers = parser.add_subparsers(dest="command")

    # find command
    find_parser = subparsers.add_parser("find", help="Find good first issues")
    find_parser.add_argument("--language", "-l", help="Programming language (e.g. python, go)")
    find_parser.add_argument("--repo", "-r", help="Specific repo (e.g. mattermost/mattermost)")
    find_parser.add_argument("--limit", "-n", type=int, default=10, help="Number of results")

    # swag command
    swag_parser = subparsers.add_parser("swag", help="List companies with swag programs")
    swag_parser.add_argument("--difficulty", "-d", help="Filter by difficulty (easy, medium, hard)")

    args = parser.parse_args()

    if args.command == "find":
        find_issues(args)
    elif args.command == "swag":
        list_swag(getattr(args, "difficulty", None))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()