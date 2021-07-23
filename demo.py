from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\ramac\\Downloads\\chromedriver_win32\\chromedriver.exe")

print(type(driver))

driver.get("http://www.google.com")
mypageTitle = driver.title
print(mypageTitle)

print(driver.quit)


driver.quit()




