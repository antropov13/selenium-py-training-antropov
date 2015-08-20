from php4dvd.pages.page import Page
from selenium.webdriver.common.by import By

class InternalPage(Page):

    @property
    def logout_button(self):
         return self.driver.find_element_by_css_selector("nav a[href $= '?logout']")

    @property
    def home_button(self):
         return self.driver.find_element_by_css_selector("nav > ul > li > a")

    @property
    def user_management_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?go=users']")

    @property
    def user_profile_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?go=profile']")

    @property
    def add_movie_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?go=add']")

    @property
    def search_movie(self):
        return self.driver.find_element_by_id("q")

    @property
    def not_found_movie(self):
        return self.driver.find_element_by_css_selector("#results > div.content")

    @property
    def name_result_film(self):
        return self.driver.find_elements_by_css_selector("#results > a > div.movie_box > div.title")

    @property
    def return_film(self):
        return self.driver.find_element_by_css_selector("#results > a > div.movie_box")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.ID, "results"))