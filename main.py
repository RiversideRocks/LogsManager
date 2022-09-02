import requests
from bs4 import BeautifulSoup
import os
import dns
import dns.resolver
import sys

blacklist = ["myvzw.com", "spectrum.com", "comcast.net", "netvigator.com", "reverse-mundo-r.com", "naturalwireless.com"]

# Note to self: consider skipping the first domain file. It contains mostly ISP domains
# that tend to include nothing of use

f = os.listdir('lists')
for stuff in f:
    if ".txt" in stuff:
        with open('lists/' + stuff) as f:
            for url in f: # url is the url, and c is the counter
                if [bad for bad in blacklist if(bad in url)]:
                    print("Skipped")
                else:
                    # ADD THIS BACK LATER BECAUSE AT ONE
                    # POINT IT WORKED
                    #try:
                    #    result = dns.resolver.query(url, 'A')
                    #    for ipval in result:
                    #        print('IP', ipval.to_text())
                    #except:
                    #    print("BAD URL!!!!")
                    print(url)

url = "https://www.fbi.gov"
html = requests.get(url, headers={"User-agent": "Master 1337 Hacker"})
soup = BeautifulSoup(html.text, "html.parser")
print(soup.title)