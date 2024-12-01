#install selenium
#install chromium chrome driver
#install google-chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup as bs
import time
service = Service("/home/shreyas27/fish/Lib-related/soup/webscrapai/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=service)
print(f'Company_Name, Mobile_No, Email, Address, No_of_Plants')
driver.get("https://upnedasolarrooftopportal.com/Approved-Firms")

try:
    wait =  WebDriverWait(driver, 10)
    element1 = wait.until(EC.element_to_be_clickable((By.TAG_NAME,'tr')))
    data_entire = driver.find_elements(By.TAG_NAME, "tr")
    for block in range(2,len(data_entire)):
        vendor_data = data_entire[block].find_elements(By.TAG_NAME, "td")
        details=[]
        for j in vendor_data:
            lll=j.text
            cleanline=" ".join(item.strip() for item in lll.split(','))
            details.append(cleanline)
        #print(details)
        #print(f'Company Name:{details[0]}\nMobile No:{details[2]}\nEmail:{details[3]}\nAddress:{details[4]}\nNo. of Plants:{details[6]}')
        print(f'{details[0]}, {details[2]}, {details[3]}, {details[4]}, {details[6]}')
finally:
    time.sleep(10)
    driver.quit()

