import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

all_links = links + links2
all_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['score'], reverse=True)


def create_custom_hn(sites, points):
    hn = []
    counter = 0
    for idx, item in enumerate(sites):
        title = sites[idx].getText()
        href = sites[idx].get('href', None)
        vote = points[idx].select('.score')
        if len(vote):
            score = int(vote[0].getText().replace(' points', ''))
            if score > 99:
                hn.append({'title': title, 'link': href, 'score': score})
                counter += 1
    print(counter)
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(all_links, all_subtext))
