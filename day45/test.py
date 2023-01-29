from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")

contents = response.text
soup = BeautifulSoup(contents, 'html.parser')
anchor_tags = soup.find_all('span', class_='titleline')
span_elm = soup.find_all(class_='score')
for idx, tag in enumerate(anchor_tags):
    print(tag.get_text())
    print(tag.find('a').get('href'))

    try:
        print(int(span_elm[idx].get_text().split()[0]))
    except IndexError:
        print("Upvote not found")



