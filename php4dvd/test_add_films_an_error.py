from php4dvd.model.user import User
#from selenium_fixture import app

def test_login(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

def test_add_film_error(app):
    movies_to = len(app.result_film())
    #name = 'Мстители: Эра Альтрона'
    year = '2015'
    cast = ("Роберт Дауни мл.", "Крис Хемсворт", "Крис Эванс")
    app.add_film_error(year, cast)
    movies_after = app.result_film()
    assert movies_to == len(movies_after)

def test_logout(app):
    app.logout()
    assert app.is_not_logged_in()
