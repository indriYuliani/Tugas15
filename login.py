import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 

        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("testerjago") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data, 'Welcome tester jago')
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_b_failed_login_with_empty_email(self):
        
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("testerjago") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data, 'Email tidak valid')
        self.assertEqual(response_message, 'Cek kembali email anda')

    def test_c_failed_login_with_empty_password(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data, "User's not found")
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_d_failed_login_with_wrong_password(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("xxxxxx") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data, "User's not found")
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def tearDown(self): 
        self.driver.close() 
    
    def test_d_failed_login_with_empaty_email_and_password(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data, "Email tidak valid")
        self.assertEqual(response_message, 'Cek kembali email anda')

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()