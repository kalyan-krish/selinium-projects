from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\ramac\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
print("Scan QR code with your mobile whatsapp")
time.sleep(5)
input()
print("logged in")

contact = 'Ravi'
search_box = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")

search_box.send_keys(contact)
search_box.send_keys(Keys.ENTER)
time.sleep(5)

message_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
message_box.send_keys("Hi Ravi this message is sent by automation program")
message_box.send_keys(Keys.ENTER)


