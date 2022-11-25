import requests
import lxml.html as lh
import pandas as pd

def chunk(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

url = 'https://jlptsensei.com/jlpt-n2-kanji-list/'

page = requests.get(url)

doc = lh.fromstring(page.content)

th_elements = doc.xpath('//th')

column_titles = []

for th in th_elements:
    column_titles.append(th.text_content())

td_elements = doc.xpath('//td')

column_data = []

for td in td_elements:
    column_data.append(td.text_content())

column_data = list(filter(('       (adsbygoogle = window.adsbygoogle || []).push({});   ').__ne__, column_data))

splited_data = list(chunk(column_data, 5))

df = pd.DataFrame(splited_data, columns=column_titles)

df = df.drop(['#'], axis=1)

data = df.to_csv(encoding='utf-16')

with open("./data/N2.csv", "w", encoding="utf-16") as f:
    f.write(data)