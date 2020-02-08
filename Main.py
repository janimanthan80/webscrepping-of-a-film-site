import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://entretenimento.uol.com.br/filmes-e-series',
    'https://www.uol.com.br/esporte/'
    )

soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(class_ = 'collection-index')
# week1 = soup.find(class_ = 'six-highlights-with-photo')
# print(week,week1)
# print(week)
list1 = week.find_all(class_ = 'thumbnail-standard')
# print(list1)

print(list1[0].find(class_ = 'thumb-title').get_text())

# print(list1[0].find(class_ = 'thumb-description').get_text())

print(list1[0].find(class_ = 'thumb-time').get_text())

thumb_title = [list1.find(class_ = 'thumb-title').get_text() for list1 in list1]


thumb_time = [list1.find(class_ = 'thumb-time').get_text() for list1 in list1]

# print(thumb_title)
# # # print(thumb_description)
# print(thumb_time)

entertainment_stuff = pd.DataFrame(
  {
    'thumb-title': thumb_title,
    'thumb-time': thumb_time,
  }
)

print(entertainment_stuff)

entertainment_stuff.to_csv('entertainment_stuff.csv')
