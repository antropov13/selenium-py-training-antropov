from php4dvd.model.user import User
from php4dvd.pages.film_page_info import FilmInfoPage
from php4dvd.pages.add_film_page import AddFilmPage
from php4dvd.pages.internal_page import InternalPage
from php4dvd.pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *


class Application(object):
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.add_film_page = AddFilmPage(driver, base_url)
        self.film_info_page = FilmInfoPage(driver, base_url)

    def logout(self):
        self.internal_page.logout_button.click()
        self.wait.until(alert_is_present()).accept()

    def ensure_logout(self):
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, #loginform")))
        if element.tag_name == "nav":
            self.logout()

    def login(self, user):
        lp = self.login_page
        lp.is_this_page
        lp.username_field.send_keys(user.username)
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()

    def ensure_login_as(self, user):
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, #loginform")))
        if element.tag_name == "nav":
            # we are on internal page
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
        self.login(user)

    def is_logged_in(self):
        return self.internal_page.is_this_page

    def is_logged_in_as(self, user):
        return self.is_logged_in() \
            and self.get_logged_user().username == user.username

    def is_not_logged_in(self):
        return self.login_page.is_this_page

    def is_addfilm_page(self):
        return self.add_film_page.is_this_page

    def add_film(self, name_film, year_film, cast):
        from selenium.webdriver.common.keys import Keys
        ip = self.internal_page
        ip.add_movie_link.click()
        ad = self.add_film_page
        ad.is_this_page
        ad.input_name_film.send_keys(name_film)
        ad.input_year_film.send_keys(year_film)
        for element in cast:
            ad.input_cast_film.send_keys(element)
            ad.input_cast_film.send_keys(Keys.RETURN)
        ad.submit_button.click()
        self.add_film_info(name_film, year_film, cast)

    def add_film_error(self, year_film, cast):
        from selenium.webdriver.common.keys import Keys
        ip = self.internal_page
        ip.add_movie_link.click()
        ad = self.add_film_page
        ad.is_this_page
        #ad.input_name_film.send_keys(name_film)
        ad.input_year_film.send_keys(year_film)
        for element in cast:
            ad.input_cast_film.send_keys(element)
            ad.input_cast_film.send_keys(Keys.RETURN)
        ad.submit_button.click()
        self.add_film_page.is_this_page
        self.internal_page.home_button.click()
        self.internal_page.is_this_page


    def add_film_info(self, name_film, year_film, cast):
        filminfo = self.film_info_page
        filminfo.is_this_page
        name = filminfo.input_name_film
        assert name == name_film+" ("+year_film+")"
        casts = filminfo.input_cast_film
        i=0
        for element in casts:
            self.to_compare_text2(element,cast[i])
            i=i+1
        self.internal_page.home_button.click()
        self.internal_page.is_this_page

    def check_name_film(self, movies_after, name):
        for movie in movies_after:
            try:
                if name == movie.text:
                    break
            except: pass
        else:
            self.fail("error movie add")

    def to_compare_text2(self,text1,text2):
        if text1==text2:
            return True
        else:
            self.fail(text1+" != "+ text2)

    def result_film(self):
        return self.internal_page.name_result_film

    def delete_film(self):
        ip = self.internal_page
        movi = ip.return_film
        movi.click()
        filminfo = self.film_info_page
        filminfo.is_this_page
        filminfo.button_delete.click()
        self.wait.until(alert_is_present()).accept()

    def found_film(self, film):
        from selenium.webdriver.common.keys import Keys
        ip = self.internal_page
        ip.is_this_page
        ip.search_movie.click()
        ip.search_movie.send_keys(film)
        ip.search_movie.send_keys(Keys.RETURN)

    def not_found_film(self):
        self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "#results > div.content")))
        return self.internal_page.not_found_movie.text

    def current_url(self):
        return self.driver.current_url

    def is_url_page(self,url1):
        for i in range(100):
            try:
                url_current = self.driver.current_url
                if url1 != url_current:
                    return True
            except: pass
        else:
            self.fail("time out")

    def search_film_filter(self, movies_filter,search_movie):
        for movie in movies_filter:
            film = movie.text
            if film.find(search_movie) > (-1):
                pass
            else:
                self.fail("search movie: "+film)






