from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


html_text = requests.get('https://www.reddit.com/').text
soup = BeautifulSoup(html_text , 'lxml')
titles = soup.find_all('a' , class_ = 'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE')
times = soup.find_all('span' , class_ = '_2VF2J19pUIMSLJFky-7PEI')
subs = soup.find_all('a' , class_ = '_3ryJoIoycVkA88fy40qNJc')

tle = []
tme = []
sb = []

for block in titles:
    title = block.find('h3' , class_ = '_eYtD2XCVieq6emjKBH3m').text
    tle.append(title)

for timestamp in times:
    tme.append(timestamp.text)

for sub in subs:
    sb.append(sub['href'].replace('/' , '' , 1))

df = pd.DataFrame(list(zip(tle , tme , sb)) , columns = ["Title" , "TimeStamp" , "Sub"])
print(df)
df.to_excel("WnCCData.xls" , index = False)
