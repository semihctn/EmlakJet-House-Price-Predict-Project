

from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.arabam.com/ikinci-el?take=50&page=1').text

#print(html_text)
soup = BeautifulSoup(html_text,'lxml')
models = soup.find_all('tr', class_='listing-list-item pr should-hover bg-white')
for model in models:
    model_name = model.find('td', class_='listing-modelname pr').text
    title = model.find('td', class_='horizontal-half-padder-minus pr').text
    model_year = model.find('td', class_='listing-text pl8 pr8 tac pr').text
    price = model.find('td', class_='pl8 pr8 tac pr').text.replace('TL','').replace(' ','').replace('.','')
    publish_date = model.find('td', class_='listing-text tac pr').text
    location = model.find('div' , class_='pr', style='display:flex;justify-content:center;align-items:center;height:81px').text.split(' ', 1)[0]
    print("{" + "\"model_name\":\"" + model_name + "\"" + "," + "\"title\":" + "\"" + title + "\",\"" + "model_year\"" + ":\"" + model_year + "\"" + ",\"price\":\"" + price + "\"" + ",\"publish_date\":\"" + publish_date + "\"," + "\"location\":\"" + location + "\"}")
