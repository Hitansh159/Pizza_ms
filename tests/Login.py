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


class TestEmptyonlyonefield():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_emptyonlyonefield(self):
    self.driver.get("http://127.0.0.1:8000/auth/")
    self.driver.set_window_size(1069, 808)
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("123456789")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    assert self.driver.title == "Login"


class TestBacktosigninpage():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_backtosigninpage(self):
    self.driver.get("http://127.0.0.1:8000/auth/")
    self.driver.set_window_size(1073, 808)
    self.driver.find_element(By.CSS_SELECTOR, "u").click()

class TestLoginsuccessfully():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_loginsuccessfully(self):
    self.driver.get("http://127.0.0.1:8000/auth/")
    self.driver.set_window_size(1077, 808)
    self.driver.find_element(By.ID, "id").click()
    self.driver.find_element(By.ID, "id").send_keys("admin")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("admin")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    assert self.driver.title == "Pizza GO - order"

class TestSQLInjection():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_SQLInjection(self):
    self.driver.get("http://127.0.0.1:8000/auth/")
    self.driver.set_window_size(1077, 808)
    self.driver.find_element(By.ID, "id").click()
    self.driver.find_element(By.ID, "id").send_keys("' OR 1=1--'")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    assert self.driver.title == "Login"
