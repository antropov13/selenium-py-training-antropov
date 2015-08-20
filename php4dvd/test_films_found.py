from php4dvd.model.user import User
#from selenium_fixture import app

def test_login(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

def test_found_film(app):
    movies_to = len(app.result_film())
    assert movies_to>0
    current_url = app.current_url()
    search_film = "Мстители"
    app.found_film(search_film)
    app.is_url_page(current_url)
    movies_after = app.result_film()
    assert len(movies_after)<=movies_to
    app.search_film_filter(movies_after,search_film)

def test_logout(app):
    app.logout()
    assert app.is_not_logged_in()
