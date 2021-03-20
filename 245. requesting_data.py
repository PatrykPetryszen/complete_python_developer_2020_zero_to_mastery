import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.find_all('a'))
# print(soup.a)
# print(soup.title)
links = soup.select('.storylink')
votes = soup.select('.score')
print(votes[0].get('id'))

# print(links) It will print a list
#print(votes)

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links, votes):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        # print(title)
        hn.append(href)
    return hn

print(create_custom_hn(links, votes))