from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select # for drop downs to select items
import time


driver = webdriver.Chrome(executable_path="C:\\Users\\ramac\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.facebook.com/")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='pageFooter']/ul/li[8]/a").click()  # to covert the language

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a").click()

time.sleep(3)

month = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[2]")

monthDD = Select(month)

first_item = monthDD.first_selected_option #default dropdown item

print(first_item.text)

assert "May" == first_item.text

monthDD.select_by_index(3) #march

time.sleep(3)

monthDD.select_by_value('7') #july

time.sleep(3)

monthDD.select_by_visible_text("Aug") #Aug preferred option

time.sleep(3)

count_opt = monthDD.options
print(len(count_opt))



for value in count_opt:
    print("value is ", value.text)
    if value.text == 'Feb':
        value.click()
        break


