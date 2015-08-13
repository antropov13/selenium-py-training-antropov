# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
import sys
import os.path
import unittest, time, re

def is_find_element(self,by,locator):
    try:
        self.wait.until(presence_of_element_located((by, locator)))
        return True
    except WebDriverException:
        self.fail("time out: "+locator)

def to_compare_text(self,by,locator,text):
    driver = self.driver
    text_site = driver.find_element(by, locator).text
    if text.find(text_site)>(-1):
        return True
    else:
        self.fail(text_site+" != "+ text)

def to_compare_text2(self,text1,text2):
    driver = self.driver
    if text1==text2:
        return True
    else:
        self.fail(text1+" != "+ text2)

class Untitled2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
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
        driver.find_element_by_css_selector("#content > section > nav > ul > li:nth-child(1) > div > div > a").click()
        is_find_element(self, By.CSS_SELECTOR,"div.addmovie")

        name = 'Мстители: Эра Альтрона'
        year = '2015'
        taglines = 'A new age begins'
        cast = ("Роберт Дауни мл.", "Крис Хемсворт", "Крис Эванс")

        #Не заполняем одно обязательное поле
        #driver.find_element_by_name('name').send_keys(name)
        driver.find_element_by_name('year').send_keys(year)
        driver.find_element_by_name('taglines').send_keys(taglines)
        driver.find_element_by_id('own_no').click()

        #Хотел прикрепить картинку..
        #cover = os.path.abspath("img/cover.jpg")
        #driver.find_element_by_xpath("//input[@type='file']").send_keys(cover)

        #driver.find_element_by_id('cover').send_keys("img/cover.jpg")

        for element in cast:
            driver.find_element_by_name('cast').send_keys(element)
            driver.find_element_by_name('cast').send_keys(Keys.ENTER)

        driver.find_element_by_id('submit').click()
        is_find_element(self, By.CSS_SELECTOR,"div.addmovie")

        #Плохой сценарий не прошел, заполняем обязательное поле
        driver.find_element_by_name('name').send_keys(name)
        driver.find_element_by_id('submit').click()

        is_find_element(self, By.CSS_SELECTOR,"div.maininfo_full")
        #Проверка

        to_compare_text(self,By.CSS_SELECTOR,"div.maininfo_full > h2",name+" ("+year+")")
        to_compare_text(self,By.CSS_SELECTOR,"div.taglines > div",taglines)

        cast_cite = driver.find_elements_by_css_selector("div.maininfo_full > div.cast > div.castlist > div.column > ul > li")
        assert len(cast_cite) == len(cast)
        i = 0
        for element in cast_cite:
            to_compare_text2(self,element.text,cast[i])
            i=i+1

        driver.find_element_by_css_selector("div.center > nav > ul > li > a").click()
        is_find_element(self, By.ID,"results")

        movies_after = driver.find_elements_by_css_selector("#results > a > div.movie_box > div.title")
        assert len(movies_to)+1 == len(movies_after)

        for movie in movies_after:
            try:
                if name == movie.text:
                    break
            except: pass
        else:
            self.fail("error movie add")




        driver.find_element_by_css_selector("nav > ul > li:nth-child(4) > a").click()
        driver._switch_to.alert.accept()
        is_find_element(self, By.ID,"loginform")

if __name__ == "__main__":
    unittest.main()
