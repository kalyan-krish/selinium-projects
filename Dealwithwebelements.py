from selenium import webdriver

driver = webdriver.Edge(executable_path="C:\\Users\\ramac\\Downloads\\edgedriver_win64 (1)\\msedgedriver.exe")


driver.maximize_window()

driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

username = driver.find_element_by_name("identifier")

username.send_keys("ramachandruni6@gmail.com")

next = driver.find_element_by_class_name("VfPpkd-RLmnJb")

next.click()

#password = driver.find_element_by_id("pseudonym_session_password")

#password.send_keys("Kalyan276@")

#login_button = driver.find_element_by_class_name("button")

#login_button.click()
