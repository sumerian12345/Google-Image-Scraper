# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#download webdriver for chrome https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome('C:/Users/Admin/Downloads/chromedriver_win32/chromedriver.exe') #location of chromedriver exe file
driver.get('https://www.google.com/')

box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

##CHANGE THE KEYWORDS BELOW FOR DESIRED SEARCH RESULTS
box.send_keys('baby yoda pictures')
##CHANGE KEYWORDS HERE FOR DESIRED SEARCH RESULTS

box.send_keys(Keys.ENTER)

driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click() #//*[@id="hdtb-msb"]/div[1]/div/div[2]/a

#keep scrolling till the end

last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click() #may have to change this. //*[@id="hdtb-msb"]/div[1]/div/div[2]/a
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

for i in range(1,50): #This means I want 50 images.
    try:
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('C:\\Users\\Admin\\Google Drive\\AIA Studio\\00-Datasets\\02-Images\\baby yoda\\baby yoda ('+str(i)+').png') #this is where you set the folder. Make the folder beforehand.
    except:
        pass