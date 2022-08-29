import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20220328132419if_/https://dataset.domainsproject.org/generic_com/"
html = requests.get(url, headers={"User-agent": "RiversideRocks (+https://riverside.rocks)"})
soup = BeautifulSoup(html.text, "html.parser")
links = soup.find_all('a')
for link in links:
    if ".txt" in link['href']:
        print(link['href'])
        #href = requests.head("https://web.archive.org/web/20220328142042if_/https://dataset.domainsproject.org/generic_com/" + link['href'], headers={"User-agent": "RiversideRocks (+https://riverside.rocks)"})
        #print(href.status_code)