from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\ramac\\Downloads\\chromedriver_win321\\chromedriver.exe")

driver.get("https://www.google.com/gmail/")

username = 'ramachandruni6'

driver.find_element_by_xpath("//*[@id='identifierId']").send_keys(username,Keys.ENTER)




