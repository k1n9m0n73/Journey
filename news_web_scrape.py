import pandas as pd
import requests
from bs4 import BeautifulSoup

#insert page URL
URL = 'https://www.sunnewsonline.com/?p=*****'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

#find main content block
news = soup.find(class_='site-main clearfix')

#print(news)

#find all the news block on block
items = news.find_all(class_='jeg_post jeg_pl_md_2 format-standard')

#find items(i.e title, summary, link, date)
#print(items[0].find(class_='seg-title').get_text())
#print(items[0].find('a').get('href'))
#print(items[0].find(class_='seg-summary').get_text())
#print(items[0].find(class_='seg-time').get_text())


title = [item.find(class_='jeg_post_title').get_text() for item in items]
link = [item.find('a').get('href') for item in items]
summary = [item.find(class_='jeg_post_excerpt').get_text() for item in items]
date = [item.find(class_='jeg_meta_date').get_text() for item in items]


#print(title)
#print(link)
#print(summary)
#print(date)

#output format
h_lines = pd.DataFrame(
    {
        'Title': title,
        'Link': link,
        'Summary': summary,
        'Date': date,
    })

print(h_lines)

#print to json or csv
h_lines.to_json('The Sun.json')