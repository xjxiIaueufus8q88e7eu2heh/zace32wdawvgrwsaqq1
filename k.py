import subprocess
import os
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
options.add_argument('/home/runner/work/zace32wdawvgrwsaqq1/zace32wdawvgrwsaqq1/xd/ip6t33by.ShitassNigga')


driver = webdriver.Firefox(options=options)

url = "https://www.youtube.com"
driver.get(url)


print(driver.title)
driver.quit()
