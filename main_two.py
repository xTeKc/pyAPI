import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
  
# keep_alive function, that maintains continious 
# running of the code.
from keep_alive import keep_alive
import pytz
  
# to start the thread
keep_alive()
while(True):
    tz_NY = pytz.timezone('Asia/Kolkata')
    datetime_NY = datetime.now(tz_NY)
      
    # this is just to get the time at the time of web scraping
    current_time = datetime_NY.strftime("%H:%M:%S - (%d/%m)")
    print(f'At time : {current_time} IST')
  
    url0 = config('URL)')
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
  
    time.sleep(60)