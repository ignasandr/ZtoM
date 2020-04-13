import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def create_custom_hn(sites, points):
    hn = []
    for idx, item in enumerate(sites):
        title = sites[idx].getText()
        href = sites[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            score = int(vote[0].getText().replace(' points', ''))

        hn.append({'title': title, 'link': href, 'score': score})
    return hn


print(create_custom_hn(links, subtext))