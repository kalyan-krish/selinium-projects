from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()

driver.implicitly_wait(15)

driver.get("https://www.google.com/maps/@20.9880135,82.7525294,5z")

search_box = driver.find_element_by_xpath("//*[@isd='searchboxinput']")

To_place = str(input("Enter the destination"))

search_box.send_keys(To_place,Keys.ENTER)
