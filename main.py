import requests 
from bs4 import BeautifulSoup
import time
from decouple import config

def show_url0():
    url0 = config('URL0')
    print(url0)