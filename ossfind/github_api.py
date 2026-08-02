import requests
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)

GITHUB_API = "https://api.github.com/search/issues"

def find_issues(args):
    print(Fore.CYAN + "\n🔍 Searching for open source issues...\n")
    
    query = "is:open is:issue label:\"good first issue\""
    
    if args.language:
        query += f" language:{args.language}"
    
    if args.repo:
        query += f" repo:{args.repo}"
    
    params = {
        "q": query,
        "sort": "created",
        "order": "desc",
        "per_page": args.limit
    }
    
    try:
        response = requests.get(GITHUB_API, params=params)
        response.raise_for_status()
        data = response.json()
        
        if not data["items"]:
            print(Fore.YELLOW + "No issues found! Try different filters.")
            return
        
        table = []
        for issue in data["items"]:
            repo = issue["repository_url"].replace("https://api.github.com/repos/", "")
            table.append([
                repo,
                issue["title"][:50] + "..." if len(issue["title"]) > 50 else issue["title"],
                issue["html_url"]
            ])
        
        print(tabulate(table, headers=["Repo", "Issue", "Link"], tablefmt="grid"))
        print(Style.RESET_ALL)
        
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error: {e}")