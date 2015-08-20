from pages.page import Page
from selenium.webdriver.common.by import By

class AddFilmPage(Page):

    @property
    def input_year_film(self):
        return self.driver.find_element_by_name("year")

    @property
    def input_name_film(self):
        return self.driver.find_element_by_name("name")

    @property
    def input_taglines_film(self):
        return self.driver.find_element_by_name("taglines")

    @property
    def input_cast_film(self):
        return self.driver.find_element_by_name("cast")

    @property
    def input_taglines_film(self):
        return self.driver.find_element_by_id("own_no")

    @property
    def submit_button(self):
        return self.driver.find_element_by_name("submit")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "div.addmovie"))

    @property
    def is_this_page_info_film(self):
        return self.is_element_visible((By.CSS_SELECTOR, "div.maininfo_full"))