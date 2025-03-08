import subprocess
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#save the url as a variable
from selenium.webdriver.firefox.service import Service
options = Options()
options.add_argument('-headless')
options.add_argument("--log-level=3")
options.add_argument("-profile")
options.add_argument('/home/runner/work/zace32wdawvgrwsaqq1/zace32wdawvgrwsaqq1/ip6t33by.ShitassNigga')

driver = webdriver.Firefox(service=Service("/home/runner/work/zace32wdawvgrwsaqq1/zace32wdawvgrwsaqq1/geckodriver"), options=options)

url = "https://www.youtube.com"
driver.get(url)
import os
if not os.path.exists('shit'):
   os.makedirs('shit')
print(driver.title)
time.sleep(20)
driver.save_screenshot("/home/runner/work/zace32wdawvgrwsaqq1/zace32wdawvgrwsaqq1/shit/d5.png")
#wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
#x_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"buttons\"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")))
#print(x_button.text)
#print(dir(x_button))
#x_button.click()
#driver.save_screenshot("/home/runner/work/zace32wdawvgrwsaqq1/zace32wdawvgrwsaqq1/shit/d4.png")
#y_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-compact-link-renderer:nth-of-type(1) div:nth-of-type(2) > yt-formatted-string:nth-of-type(1)")))
#y_button.click()
#time.sleep(20)
#driver.save_screenshot("/home/runner/work/zace32wdawvgrwsaqq1/zace32wdawvgrwsaqq1/shit/d5.png")
driver.quit()
