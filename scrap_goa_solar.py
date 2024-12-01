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
print('Company_name, Address, City, Scheme_Name, Category, Mobile, Email-ID')
driver.get("https://goasolar.in/installers")
try:
    for i in range(8):
        wait = WebDriverWait(driver, 10)
        element1 = wait.until(EC.element_to_be_clickable((By.TAG_NAME,'tr')))
        data1 = driver.find_elements(By.TAG_NAME, "tr")
        for d in range(1,len(data1)):
            #html_source=link.get_attribute("innerHTML")
            rl_data=data1[d].find_elements(By.TAG_NAME,"td")
            l=[]
            for j in rl_data:
                lll=j.text
                cleanline=" ".join(item.strip() for item in lll.split(','))
                l.append(cleanline)
            #print(len(l))
            #print(f'Company name:{l[0]}\nAddress:{l[1]}\nCity:{l[2]},{l[3]}\nScheme Name:{l[4]}\nCategory:{l[5]}\nMobile:{l[6]}\nEmail-ID:{l[7]}')
            #print("\n")
            print(f'{l[0]},{l[1]},{l[2]} {l[3]},{l[4]},{l[5]},{l[6]},{l[7]}')
        if(i!=7):
            page_change=driver.find_element(By.XPATH,"//a[@href='/installers/"+str(i+2)+"']")
            page_change.click()
        else:
            break

finally:
#element=driver.find_element(By.XPATH,'//*[@id="search-container"]')
#element.send_keys("some text")
    time.sleep(10)
    driver.quit()

