import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pytest_html_reporter import attach

class TestNot10characternumber():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_not10characternumber(self):
        self.driver.get("http://127.0.0.1:8000/auth/signup")
        self.driver.set_window_size(1054, 808)
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("user60")
        self.driver.find_element(By.ID, "id").click()
        self.driver.find_element(By.ID, "id").send_keys("tejasVBorkar@gmail.com")
        self.driver.find_element(By.ID, "id").click()
        self.driver.find_element(By.ID, "id").click()
        self.driver.find_element(By.ID, "id").send_keys("tejasVBorkar123@gmail.com")
        self.driver.find_element(By.NAME, "phone").click()
        self.driver.find_element(By.NAME, "phone").send_keys("32323232322")
        self.driver.find_element(By.NAME, "phone").click()
        self.driver.find_element(By.NAME, "phone").send_keys("32323232")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("123456789")
        self.driver.find_element(By.ID, "confirm_password").click()
        self.driver.find_element(By.ID, "confirm_password").send_keys("123456789")
        self.driver.find_element(By.ID, "submit").click()
        assert self.driver.title == "Pizza Go Signup"
        attach(data=self.driver.get_screenshot_as_png())


class TestBacktologinpage():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_backtologinpage(self):
        self.driver.get("http://127.0.0.1:8000/auth/signup")
        self.driver.set_window_size(1061, 808)
        self.driver.find_element(By.CSS_SELECTOR, "u").click()


class TestWrongEmailId():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_wrongEmailId(self):
        self.driver.get("http://127.0.0.1:8000/auth/signup")
        self.driver.set_window_size(1051, 806)
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("user30")
        self.driver.find_element(By.ID, "id").click()
        self.driver.find_element(By.ID, "id").send_keys("Tejas V Borkar")
        self.driver.find_element(By.NAME, "phone").click()
        self.driver.find_element(By.NAME, "phone").send_keys("98919088413")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("123456789")
        self.driver.find_element(By.ID, "confirm_password").click()
        self.driver.find_element(By.ID, "confirm_password").send_keys("123456789")
        self.driver.find_element(By.ID, "submit").click()
        assert self.driver.title == "Pizza Go Signup"
        attach(data=self.driver.get_screenshot_as_png())


class TestSameusername():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_sameusername(self):
        self.driver.get("http://127.0.0.1:8000/auth/signup")
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("user20")
        self.driver.find_element(By.CSS_SELECTOR, "#signUpForm").click()
        self.driver.find_element(By.ID, "id").click()
        self.driver.find_element(By.ID, "id").send_keys("tejasVBorkar@gmail.com")
        self.driver.find_element(By.NAME, "phone").click()
        self.driver.find_element(By.NAME, "phone").send_keys("9819088413")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("123456789")
        self.driver.find_element(By.ID, "confirm_password").click()
        self.driver.find_element(By.ID, "confirm_password").send_keys("123456789")
        self.driver.find_element(By.ID, "submit").click()
        assert self.driver.title == "Pizza Go Signup"
        attach(data=self.driver.get_screenshot_as_png())


class TestPasswordsAreNotSame():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_passwordsAreNotSame(self):
        self.driver.get("http://127.0.0.1:8000/auth/signup")
        self.driver.set_window_size(1054, 808)
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("user10")
        self.driver.find_element(By.ID, "id").click()
        self.driver.find_element(By.ID, "id").send_keys("tejasVBorkar@gmail.com")
        self.driver.find_element(By.NAME, "phone").click()
        self.driver.find_element(By.NAME, "phone").click()
        self.driver.find_element(By.NAME, "phone").send_keys("9819088413")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("12121312121")
        self.driver.find_element(By.ID, "confirm_password").click()
        self.driver.find_element(By.ID, "confirm_password").send_keys("323232")
        assert self.driver.title == "Pizza Go Signup"
        attach(data=self.driver.get_screenshot_as_png())


class TestEmptyonlyonefield():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_emptyonlyonefield(self):
        self.driver.get("http://127.0.0.1:8000/auth/signup")
        self.driver.set_window_size(1054, 808)
        self.driver.find_element(By.ID, "id").click()
        self.driver.find_element(By.ID, "id").send_keys("tejasVBorkar@gmail.com")
        self.driver.find_element(By.NAME, "phone").click()
        self.driver.find_element(By.NAME, "phone").send_keys("989099413")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("123456789")
        self.driver.find_element(By.ID, "confirm_password").click()
        self.driver.find_element(By.ID, "confirm_password").send_keys("123456789")
        self.driver.find_element(By.ID, "submit").click()
        assert self.driver.title == "Pizza Go Signup"
        attach(data=self.driver.get_screenshot_as_png())


class TestEmptyalltheinputs():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_emptyalltheinputs(self):
        self.driver.get("http://127.0.0.1:8000/auth/signup")
        self.driver.set_window_size(1054, 808)
        self.driver.find_element(By.ID, "submit").click()
        assert self.driver.title == "Pizza Go Signup"
        attach(data=self.driver.get_screenshot_as_png())

class TestSigninsuccessfully():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}


    def teardown_method(self, method):
        self.driver.quit()


    def test_signinsuccessfully(self):
        self.driver.get("http://127.0.0.1:8000/auth/signup")
        self.driver.set_window_size(1058, 808)
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("user100")
        self.driver.find_element(By.ID, "id").click()
        self.driver.find_element(By.ID, "id").send_keys("tejasVBorkar1@gmail.com")
        self.driver.find_element(By.NAME, "phone").click()
        self.driver.find_element(By.NAME, "phone").send_keys("9819088413")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("123456789")
        self.driver.find_element(By.ID, "confirm_password").click()
        self.driver.find_element(By.ID, "confirm_password").send_keys("123456789")
        self.driver.find_element(By.ID, "submit").click()
        assert self.driver.title == "Login"
        attach(data=self.driver.get_screenshot_as_png())