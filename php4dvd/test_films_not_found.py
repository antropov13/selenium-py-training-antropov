from php4dvd.model.user import User
#from selenium_fixture import app



def test_login(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

def test_found_film(app):
    movies_to = len(app.result_film())
    assert movies_to>0
    app.found_film("=867=-5=0-6045-")
    text = app.not_found_film()
    assert text == 'No movies where found.'

def test_logout(app):
    app.logout()
    assert app.is_not_logged_in()

