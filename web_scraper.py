import requests
from bs4 import BeautifulSoup
import urllib3
from urllib.parse import urljoin

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = input("Enter website URL: ")

# Headers to avoid blocking
headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(url, headers=headers, verify=False, timeout=10)

    # Check if request successful
    if response.status_code != 200:
        print(" Failed to retrieve webpage (Status Code:", response.status_code, ")")
    else:
        soup = BeautifulSoup(response.text, "html.parser")

        print("\n Cleaned Links:\n")

        links = set()  # to remove duplicates

        for link in soup.find_all("a"):
            href = link.get("href")

            if href:
                full_url = urljoin(url, href)

                # Filter only proper http/https links
                if full_url.startswith("http"):
                    links.add(full_url)

        if links:
            for link in links:
                print(link)
        else:
            print(" No links found on this page.")

except requests.exceptions.RequestException as e:
    print(" Error:", e)