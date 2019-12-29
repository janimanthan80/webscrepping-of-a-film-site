import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=25.7748&lon=-80.1977#.XgZ_f0dKhEY'
    )

soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id = 'seven-day-forecast-body')
# print(week)

items = (week.find_all(class_='tombstone-container'))
# print(items)

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_name = [items.find(class_='period-name').get_text() for items in items]
short_descriptions = [items.find(class_='short-desc').get_text() for items in items]
tempuratures = [items.find(class_='temp').get_text() for items in items]

print(period_name)
print(short_descriptions)
print(tempuratures)

weather_stuff = pd.DataFrame(
    {
        'period': period_name,
        'short_descriptions': short_descriptions,
        'tempuratures': tempuratures,
    }
)
print(weather_stuff)

weather_stuff.to_csv('watherstuff.csv')
