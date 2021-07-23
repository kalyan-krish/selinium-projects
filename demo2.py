from selenium import webdriver

#driver = webdriver.Ie(executable_path="C:\\Users\\ramac\\Downloads\\IEDriverServer_x64_3.150.1\\IEDriverServer.exe")

driver = webdriver.Chrome(executable_path="C:\\Users\\ramac\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("http://www.google.com")

driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys('sb')

list_elements = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/ul/li[1]")

for i in list_elements:
    print(i.text)
