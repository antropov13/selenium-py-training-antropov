from php4dvd.model.user import User
#from selenium_fixture import app


def result_film(app):
    return app.result_film()

def test_login(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

def test_delete_film(app):
    movies_to = app.result_film()
    assert len(movies_to)>0
    app.delete_film()
    movies_after = app.result_film()
    assert len(movies_to)-1 == len(movies_after)

def test_logout(app):
    app.logout()
    assert app.is_not_logged_in()
