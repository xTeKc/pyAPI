import requests 
from bs4 import BeautifulSoup
import time
import datetime
from decouple import config

# def show_url0():
#     url0 = config('URL0')
#     response = requests.get(url0)
#     text = response.text
#     data = BeautifulSoup(text, 'html.parser')
#     # print(url0)

#     # first row of table (tr) = top row
#     headings = data.find_all('tr')[0]
#     headings_list = [] # list to store all headings

#     # get set amount of columns
#     headings_list = headings_list[:10]

#     print('Headings are: ')
#     for column in headings_list:
#         print(column)

    
#     # since we need only first five coins
#     for x in range(1, 6):
#         table = data.find_all('tr')[x]
#         c = table.find_all('td')

#         for x in c:
#             print(x.text, end=' ')
#         print('')

# show_url0()

while(True):
    now = datetime.datetime.now()
      
    # this is just to get the time at the time of
    # web scraping
    current_time = now.strftime("%H:%M:%S")
    print(f'At time : {current_time} IST')
  
    url0 = config('URL0')
    response = requests.get(url0)
    text = response.text
    html_data = BeautifulSoup(text, 'html.parser')
    headings = html_data.find_all('tr')[0]
    headings_list = []
    for x in headings:
        headings_list.append(x.text)
    headings_list = headings_list[:10]
  
    data = []
  
    for x in range(1, 6):
        row = html_data.find_all('tr')[x]
        column_value = row.find_all('td')
        dict = {}
          
        for i in range(10):
            dict[headings_list[i]] = column_value[i].text
        data.append(dict)
          
    for coin in data:
        print(coin)
        print('')
    time.sleep(600)