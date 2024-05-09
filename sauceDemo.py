from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Test_Sauce:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        
    def test_invalid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//h3[@data-test='error']")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU:  {testResult}")

    def empty_password_box(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//h3[@data-test='error']")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"TEST SONUCU:  {testResult}")

    def test_lockedout_user(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("locked_out_user")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//h3[@data-test='error']")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU:  {testResult}")

    def test_listed_products(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        if "inventory.html" in self.driver.current_url:
            print("Giriş başarılı.")
        else:
            print("Giriş başarısız.")
        products = self.driver.find_elements(By.CLASS_NAME,"inventory_item") 
        if len(products) == 6:
            print("Toplamda 6 ürün listelendi.")
        else:
            print("Hata: Toplamda 6 ürün listelenmedi.")

    def test_logout(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[@id='react-burger-menu-btn']")))
        menu_button = self.driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']")
        menu_button.click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"logout_sidebar_link")))
        logoutButton = self.driver.find_element(By.ID,"logout_sidebar_link")
        logoutButton.click()
        if "https://www.saucedemo.com/" in self.driver.current_url:
            print("Çıkış başarılı.")
        else:
            print("Çıkış başarısız.")


testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.empty_password_box()
testClass.test_lockedout_user()
testClass.test_listed_products()
testClass.test_logout()


        