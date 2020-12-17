import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get('https://weather.com/weather/tenday/l/4b466aee02eb699325a58c9501e413d890bd7a6bdb09de0d1cc90797b7a954e1')
soup = BeautifulSoup(page.content, 'html.parser')

ten_days = soup.find(class_='DailyForecast--DisclosureList--350ZO')

#print(ten_days)

items = ten_days.find_all(class_='DaypartDetails--DetailSummaryContent--1c28m')

#print(items[0].find(class_='DetailsSummary--daypartName--1Mebr').get_text())
#print(items[0].find(class_='DetailsSummary--temperature--3FMlw').get_text())
#print(items[0].find(class_='DetailsSummary--condition--mqdxh').get_text())
#print(items[0].find(class_='DetailsSummary--precip--2ARnx').get_text())
#print(items[0].find(class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').get_text())

day = [item.find(class_='DetailsSummary--daypartName--1Mebr').get_text() for item in items]
temperature = [item.find(class_='DetailsSummary--temperature--3FMlw').get_text() for item in items]
condition = [item.find(class_='DetailsSummary--condition--mqdxh').get_text() for item in items]
precipitation = [item.find(class_='DetailsSummary--precip--2ARnx').get_text() for item in items]
wind = [item.find(class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').get_text() for item in items]

#print(day)
#print(temperature)
#print(condition)
#print(precipitation)
#print(wind)


weather = pd.DataFrame(
    {
        'Day': day,
        'Temperature(ºF)': temperature,
        'Condition': condition,
        'Precipitation': precipitation,
        'Wind': wind,
    })

print(weather)

weather.to_csv('Abuja weather.csv')