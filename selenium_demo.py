""" A simple demo of Selenium browser automation """
import os

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
CHROME_PATH = os.path.join(FOLDER_PATH, 'chromedrivers', 'chromedriver')
SEARCH_XPATH = '//input[@name="q"]'

driver = webdriver.Chrome(CHROME_PATH)
driver.get('https://www.google.com')

# Wait until element loads on page
search_bar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, SEARCH_XPATH))
)
search_bar.send_keys('cool cars'+Keys.RETURN)
