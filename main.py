
import requests
from bs4 import BeautifulSoup


def get_announcements(page):
    url = 'http://www.spit.ac.in/news-events/page/' + str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('h2'):
        for desc in link.findAll('a'):
            href = desc.get('href')
            for title in desc:
                announcement = title.string
                if announcement:
                    print(announcement)
                    print('Link: ' + href)
        print('\n')

n = int(input("How Many Pages Of Website(http://www.spit.ac.in/news-events/) You Want To Crawl?\n"))
for i in range(1, n + 1):
    print('<------------Page ' + str(i) + ' Announcements------------>\n')
    get_announcements(i)
print('\n')
