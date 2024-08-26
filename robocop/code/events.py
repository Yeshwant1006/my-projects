from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
eventtitle=[] #title of event
startdate=[] #starting date
enddate=[] #ending date
price=[] #price details
driver.get("<a href="https://www.eventsnow.com/">https://www.eventsnow.com/</a>")
driver.get("<a href="https://insider.in/hyderabad/">https://insider.in/hyderabad/</a>")
driver.get("<a href="https://highape.com/hyderabad/">https://highape.com/hyderabad/</a>")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':''}):
#eventsnow
eventtitle=a.find('div', attrs={'class':''})
startdate=a.find('div', attrs={'class':''})
enddate=a.find('div', attrs={'class':''})
price=a.find('div', attrs={'class':''})

eventtitle.append(title.text)
startdate.append(startdate.text)
enddate.append(enddate.text)
price.append(price.text) 

#insider
eventtitle=a.find('div', attrs={'class':''})
startdate=a.find('div', attrs={'class':''})
enddate=a.find('div', attrs={'class':''})
price=a.find('div', attrs={'class':''})

eventtitle.append(title.text)
startdate.append(startdate.text)
enddate.append(enddate.text)
price.append(price.text) 

#highape
eventtitle=a.find('div', attrs={'class':''})
startdate=a.find('div', attrs={'class':''})
enddate=a.find('div', attrs={'class':''})
price=a.find('div', attrs={'class':''})

eventtitle.append(title.text)
startdate.append(startdate.text)
enddate.append(enddate.text)
price.append(price.text) 

df = pd.DataFrame({'Eventtitle':title,'Startdate':startdate,'Enddate':enddate,'Price':price}) 
df.to_csv('events.csv', index=False, encoding='utf-8')