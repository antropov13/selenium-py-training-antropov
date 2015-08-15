# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
import sys
import unittest, time, re

def is_find_element(self,by,locator):
    try:
        self.wait.until(presence_of_element_located((by, locator)))
        return True
    except WebDriverException:
        self.fail("time out: "+locator)

class Untitled2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "http://localhost"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled2(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()

        is_find_element(self,By.CSS_SELECTOR, "nav")
        movies_to = driver.find_elements_by_css_selector("#results > a > div.movie_box > div.title")
        assert len(movies_to)>0

        #Поиск, когда что-то найдено
        driver.find_element_by_id("q").click()
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys("Мстители")
        driver.find_element_by_id("q").send_keys(Keys.RETURN)

        movies_filter = driver.find_elements_by_css_selector("#results > a > div.movie_box > div.title")
        assert len(movies_filter)>0

        driver.find_element_by_css_selector("nav > ul > li:nth-child(4) > a").click()
        driver._switch_to.alert.accept()
        is_find_element(self, By.ID,"loginform")

if __name__ == "__main__":
    unittest.main()
