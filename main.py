import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self):
        browser = self.browser
        browser.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/section/section/div[1]/div[1]/input").send_keys("student") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/section/section/div[1]/div[2]/input").send_keys("Password123") # isi Password
        time.sleep(1)
        browser.find_element(By.ID,"submit").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div/section/div/div/article/div[1]/h1").text
        self.assertEqual(response_message, 'Logged In Successfully')

    def test_a_failed_login_with_incorrect_username(self): 
        # steps
        browser = self.browser
        browser.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/section/section/div[1]/div[1]/input").send_keys("incorrectuser") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/section/section/div[1]/div[2]/input").send_keys("Password123") # isi Password
        time.sleep(1)
        browser.find_element(By.ID,"submit").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"error").text

        self.assertIn('Your username is invalid!', response_data)

    def test_a_failed_login_with_incorrect_password(self): 
        # steps
        browser = self.browser
        browser.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/section/section/div[1]/div[1]/input").send_keys("student") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/section/section/div[1]/div[2]/input").send_keys("Passwordsalah") # isi Password
        time.sleep(1)
        browser.find_element(By.ID,"submit").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"error").text

        self.assertIn('Your password is invalid!', response_data)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()