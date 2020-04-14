import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['score'], reverse=True)


def create_custom_hn(sites, points):
    hn = []
    for idx, item in enumerate(sites):
        title = sites[idx].getText()
        href = sites[idx].get('href', None)
        vote = points[idx].select('.score')
        if len(vote):
            score = int(vote[0].getText().replace(' points', ''))
            if score > 99:
                hn.append({'title': title, 'link': href, 'score': score})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))
