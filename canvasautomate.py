from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\ramac\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://canvas.instructure.com/login/canvas")

username = driver.find_element_by_name("pseudonym_session[unique_id]")

username.send_keys("ramachandruni6@gmail.com")

passwd = driver.find_element_by_name("pseudonym_session[password]")

passwd.send_keys("Kalyan276@")

driver.find_element(By.TAG_NAME,"button").click()



