from php4dvd.pages.page import Page
from selenium.webdriver.common.by import By

class FilmInfoPage(Page):

    @property
    def input_name_film(self):
        return self.driver.find_element_by_css_selector("div.maininfo_full > h2").text

    @property
    def input_cast_film(self):
        return self.driver.find_elements_by_css_selector("div.castlist > div.colomn > ul > li")

    @property
    def button_delete(self):
        return self.driver.find_element_by_css_selector("#content > section > nav > ul > li:nth-child(4) > div > div > a")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "div.maininfo_full"))