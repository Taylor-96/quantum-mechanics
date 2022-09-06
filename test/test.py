# Generated by Selenium IDE
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
from PIL import Image, ImageChops

class TestTest01():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_one_quantumwell(self):
    self.driver.get("http://localhost:8383/voila/render/index.ipynb")
    self.driver.set_window_size(1280, 720)
    self.driver.save_screenshot("index.png")
    self.driver.find_element(By.LINK_TEXT, "Numerical Solution of the Schrödinger Equation for 1D Quantum Well").click()
    time.sleep(5)
    self.driver.execute_script("window.scrollTo(0, 1000)")
    self.driver.save_screenshot("1quantumwell.png")

  def test_asymmetricwell(self):
    self.driver.get("http://localhost:8383/voila/render/index.ipynb")
    self.driver.set_window_size(1280, 720)
    self.driver.find_element(By.LINK_TEXT, "Avoided Crossing in 1D Asymmetric Quantum Well").click()
    time.sleep(5)
    self.driver.execute_script("window.scrollTo(0, 400)")
    self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(2) > input").click()
    time.sleep(10)
    self.driver.save_screenshot("asymmetricwell.png")

test = TestTest01()
test.setup_method('Chrome')
test.test_one_quantumwell()
test.teardown_method('Chrome')

test = TestTest01()
test.setup_method('Chrome')
test.test_asymmetricwell()
test.teardown_method('Chrome')

image1 = Image.open('asymmetricwell.png') 
image2 = Image.open('test/asymmetricwell.png') 

diff = ImageChops.difference(image1, image2)

if diff.getbox():
  raise Exception("The result is NOT the same as expected. Please check matplotlib version.")
else:
  print('images are the same')
