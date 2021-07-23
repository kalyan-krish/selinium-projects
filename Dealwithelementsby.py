from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\ramac\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
#username = driver.find_element_by_name("txtUsername")
driver.find_element(By.NAME,"txtUsername").send_keys("admin")
#username.send_keys("admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
#password = driver.find_element_by_id("txtPassword")
#password.send_keys("admin123")
driver.find_element(By.NAME,"Submit").click()
#login = driver.find_element_by_name("Submit")

#login.click()