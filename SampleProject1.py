from selenium import webdriver
import unittest

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\ramac\\Downloads\\chromedriver_win32\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def search_automation_stepbystep(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("youtube")
        self.driver.find_element_by_name("btnK").click()

    def search_inueron(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("inueron")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()






















