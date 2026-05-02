import requests
from bs4 import BeautifulSoup

url = input("Enter website URL: ")

try:
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "No title found"

    links = soup.find_all("a")
    images = soup.find_all("img")
    paragraphs = soup.find_all("p")

    print("\n--- Webpage Analysis ---\n")

    print("Title:", title)
    print("Total Links:", len(links))
    print("Total Images:", len(images))
    print("Total Paragraphs:", len(paragraphs))

except Exception as e:
    print("Error:", e)