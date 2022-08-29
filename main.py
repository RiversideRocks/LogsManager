import requests
from bs4 import BeautifulSoup

url = "https://www.tsa.gov"
html = requests.get(url, headers={"User-agent": "Master 1337 Hacker"})
soup = BeautifulSoup(html.text, "html.parser")
print(soup.title)