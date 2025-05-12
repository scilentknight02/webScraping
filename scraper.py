import requests
from bs4 import BeautifulSoup

req = requests.get("https://sastotickets.com/search/flight-tickets-from-Kathmandu-to-Pokhara-May-23-2025/aa0369fc-83d7-4468-b271-2a38f66f2292")
if req.status_code == 200:
    soup = BeautifulSoup(req.content, "html.parser")

    found_any = False

    for i in range(11):  # from 0 to 10
        item = soup.find(id=f"anchor-flight-summary-{i}")
        if item:
            found_any = True
            print(f"\nItem {i}:\n{item.prettify()}\n{'-'*60}")

    if not found_any:
        print("No elements with IDs from 'anchor-flight-summary-0' to 'anchor-flight-summary-20' found.")
else:
    print(f"Failed to retrieve page: {req.status_code}")
