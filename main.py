from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
from decouple import config

def get_data(data, start, end, export_csv=False):
    frames = []
    
    in_stock_url = config("IN_STOCK_URL") # IN_STOCK_URL imported from .env

    for d in data:
        the_url = in_stock_url
        option = Options()
        option.headless = False
        driver = webdriver.Chrome(options=option)
        driver.get(my_url)
        driver.maximize_window()



## Todo:
# ------
# [ X ]create gui
# [  ]import other python files
# [  ]create api or use existing api from webpage
# [  ]recognize keywords and key images?
# [  ]create functions to run other functions from other files
# [  ]add all functions to the main function and run the entire program