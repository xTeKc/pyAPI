import requests 
from bs4 import BeautifulSoup
import time
from decouple import config

def show_url0():
    url0 = config('URL0')
    response = requests.get(url0)
    text = response.text
    data = BeautifulSoup(text, 'html.parser')
    # print(url0)

show_url0()