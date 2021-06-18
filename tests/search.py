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

class TestSearch():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_search(self):
    self.driver.get("http://localhost:8000/")
    self.driver.set_window_size(890, 824)
    self.driver.find_element(By.ID, "inputSearchFood").click()
    self.driver.find_element(By.ID, "inputSearchFood").send_keys("chickn")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-outline-success").click()
    self.driver.execute_script("window.scrollTo(0, 400)") 
    self.driver.find_element(By.ID, "breads_tab").click()
    self.driver.find_element(By.ID, "drinks_desserts_tab").click()
    self.driver.find_element(By.ID, "combos_tab").click()
    self.driver.execute_script("window.scrollTo(0, 0)")
    self.driver.find_element(By.ID, "inputSearchFood").click()
    self.driver.find_element(By.ID, "inputSearchFood").send_keys("chicken")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.execute_script("window.scrollTo(0, 400)")
    self.driver.find_element(By.ID, "pizzas_tab").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) .btn").click()
    self.driver.close()
  
