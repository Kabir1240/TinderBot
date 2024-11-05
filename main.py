import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


NUMBER_OF_PEOPLE_TO_DISLIKE = 10

load_dotenv()
user_dir = os.environ.get("USER_DATA_DIR")
chrome_options = webdriver.ChromeOptions()


chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_dir}")
# chrome_options.add_argument("--incognito")


driver = webdriver.Chrome(options=chrome_options)

# Open a new tab with JavaScript
driver.execute_script("window.open('');")
# Switch to the new tab
driver.switch_to.window(driver.window_handles[-1])
driver.get("https://tinder.com/")

time.sleep(5)

dislike_button = driver.find_element(By.XPATH, "//*[@id='q1747300428']/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button")
# like_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button")


for i in range(NUMBER_OF_PEOPLE_TO_DISLIKE):
    dislike_button.click()
    time.sleep(2)
