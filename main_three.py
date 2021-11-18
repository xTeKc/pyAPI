from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

def get_data(data, start, end, export_csv=False):
    frames = []
    
    for d in data:
        my_url = f""
        option = Options()
        option.headless = False
        driver = webdriver.Chrome(options=option)
        driver.get(my_url)
        driver.maximize_window()