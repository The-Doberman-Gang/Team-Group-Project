import webbrowser
from urllib.parse import quote_plus

search_history = []

def internet_search():
    query = input("Enter a search term: ").strip()

    if not query:
        print("No search term entered.")
        return

    search_history.append(query)

    url = f"https://www.google.com/search?q={quote_plus(query)}"
    print(f"Opening browser for search: {query}")
    webbrowser.open(url)
