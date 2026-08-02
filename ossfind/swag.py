from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)

SWAG_PROGRAMS = [
    {"company": "Mattermost", "swag": "☕ Mug", "difficulty": "Easy", "how": "First PR merged", "link": "https://forum.mattermost.com/t/mattermost-first-time-contributor-mugs/143"},
    {"company": "Kong", "swag": "👕 T-shirt", "difficulty": "Medium", "how": "1 PR accepted", "link": "https://github.com/Kong/kong/blob/master/CONTRIBUTING.md"},
    {"company": "QuestDB", "swag": "👕 T-shirt", "difficulty": "Medium", "how": "Valid PR merged", "link": "https://questdb.com/community"},
    {"company": "Zulip", "swag": "👕 T-shirt", "difficulty": "Medium", "how": "Valid PR merged", "link": "https://zulip.com/contribute"},
    {"company": "GoFr", "swag": "👕 T-shirt + Stickers", "difficulty": "Medium", "how": "Notable PR or article", "link": "https://github.com/gofr-dev/gofr"},
    {"company": "Appwrite", "swag": "👕 T-shirt + Stickers", "difficulty": "Medium", "how": "Valid contribution", "link": "https://appwrite.io/community"},
    {"company": "Postman", "swag": "👕 T-shirt", "difficulty": "Medium", "how": "Notable contribution", "link": "https://www.postman.com/contributors"},
    {"company": "Gatsby x Netlify", "swag": "👕 Shirt + Stickers", "difficulty": "Hard", "how": "PR merged into Gatsby", "link": "https://www.gatsbyjs.com/contributing/contributor-swag"},
    {"company": "Hacktoberfest", "swag": "👕 T-shirt / 🌳 Tree", "difficulty": "Easy", "how": "4 PRs in October", "link": "https://hacktoberfest.com"},
    {"company": "GeeksForGeeks", "swag": "👕 T-shirt + Hoodie", "difficulty": "Medium", "how": "Solve daily problems", "link": "https://practice.geeksforgeeks.org/problem-of-the-day"},
    {"company": "IHP", "swag": "🎉 Stickers", "difficulty": "Easy", "how": "Fill out form", "link": "https://ihp.digitallyinduced.com/Stickers"},
    {"company": "JS Bin", "swag": "🎉 Stickers", "difficulty": "Easy", "how": "Fill out form", "link": "https://jsbin.com/help/stickers"},
    {"company": "devRant", "swag": "🎉 Stickers + Stress ball", "difficulty": "Medium", "how": "Get 30++ on a rant", "link": "https://devrant.com/free-stickers"},
    {"company": "DEV Podcast", "swag": "🎉 Stickers", "difficulty": "Easy", "how": "Leave a podcast review", "link": "https://airtable.com/shr8oKAIMZgdYnBxx"},
]

def list_swag(difficulty=None):
    print(Fore.CYAN + "\n🎁 Open Source Swag Programs\n")
    
    filtered = SWAG_PROGRAMS
    if difficulty:
        filtered = [p for p in SWAG_PROGRAMS if p["difficulty"].lower() == difficulty.lower()]
    
    table = [
        [p["company"], p["swag"], p["difficulty"], p["how"], p["link"]]
        for p in filtered
    ]
    print(tabulate(table, headers=["Company", "Swag", "Difficulty", "How to get", "Link"], tablefmt="grid"))
    print(Style.RESET_ALL)