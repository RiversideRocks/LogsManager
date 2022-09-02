import requests
from bs4 import BeautifulSoup
import os

f = os.listdir('lists')
for stuff in f:
    if ".txt" in stuff:
        current_file = open('lists/' + stuff, 'r')
        lines = len(current_file.readlines())
  
        c = 0
        ran_lines = current_file.readlines()
        print(lines)
        for url in current_file: # url is the url, and c is the counter
        #    c = c +1
            print(url)
        #    print("We are " + str(c) + "/" + str(ran_lines))

url = "https://www.fbi.gov"
html = requests.get(url, headers={"User-agent": "Master 1337 Hacker"})
soup = BeautifulSoup(html.text, "html.parser")
print(soup.title)