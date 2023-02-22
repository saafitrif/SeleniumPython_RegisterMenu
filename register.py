import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestRegister(unittest.TestCase):
    
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Case 1 (success navigate from sign in menu to sign up menu)
    def test_a_success_navigate_from_sign_in_menu_to_sign_up_menu(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://barru.pythonanywhere.com/daftar") #buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        
        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/form/h1").text
        self.assertIn('Create', response_data)
    
    #Test case 2 (failed register with blank name,email,and password)
    def test_a_failed_register_with_blank_name_email_and_password(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://barru.pythonanywhere.com/daftar") #buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() #klik tombol sign up
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("") #isi nama
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("") #isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("") #isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() #klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text
        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')
    
#Test case 3 (failed register with invalid email (without @))
    def test_a_failed_register_with_invalid_email_without_at(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://barru.pythonanywhere.com/daftar") #buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() #klik tombol sign up
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("aku") #isi nama
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("aku") #isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("aku") #isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() #klik tombol sign up
        time.sleep(1)

        # validasi
        email_error = browser.find_element(By.ID,"email_register").get_attribute("validationMessage")
        self.assertIn('Please', email_error)


    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
