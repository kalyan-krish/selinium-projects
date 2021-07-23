from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\ramac\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.goibibo.com/")

driver.find_element_by_xpath("//*[@id='gosuggest_inputSrc']").send_keys('ba')


