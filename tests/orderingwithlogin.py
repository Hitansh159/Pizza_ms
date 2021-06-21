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

class TestOrderingwithlogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_orderingwithlogin(self):
    self.driver.get("http://localhost:8000/")
    self.driver.set_window_size(890, 824)
    self.driver.find_element(By.ID, "inputSearchFood").click()
    self.driver.find_element(By.ID, "inputSearchFood").send_keys("chicken")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-outline-success").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(3) .btn").click()
    self.driver.find_element(By.CSS_SELECTOR, "img:nth-child(2)").click()
    self.driver.find_element(By.ID, "id").click()
    self.driver.find_element(By.ID, "id").send_keys("admin")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("admin")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "address").click()
    self.driver.find_element(By.ID, "address").send_keys("asdfg")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Log out").click()   
    self.driver.close()
  
