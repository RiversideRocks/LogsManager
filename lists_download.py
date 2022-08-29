import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20220328132419/https://dataset.domainsproject.org/generic_com/"
html = requests.get(url, headers={"User-agent": "RiversideRocks (+https://riverside.rocks)"})
soup = BeautifulSoup(html.text, "html.parser")
links = soup.find_all('a')
for link in links:
    print(link)