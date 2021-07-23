from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\\Users\\ramac\\Downloads\\chromedriver_win32\\chromedriver.exe")

#driver.maximize_window()

driver.implicitly_wait(15)

driver.get("https://www.google.com/maps/@20.9880135,82.7525294,5z")

search_box = driver.find_element_by_xpath("//*[@id='searchboxinput']")

To_place = str(input("Enter the destination"))

search_box.send_keys(To_place,Keys.ENTER)

print(driver.current_url)

directions = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div/button")

directions.click()

To_place = str(input("Enter the starting place"))

driver.find_element_by_xpath("//*[@id='sb_ifc51']/input").send_keys(To_place,Keys.ENTER)

kilometers = driver.find_element_by_xpath("//*[@id='section-directions-trip-1']/div/div[1]/div[1]")

print(kilometers.text)








