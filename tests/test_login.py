from pages.login_page import LoginPage

def test_login(driver):
    driver.get("http://www.google.com")

    login_page = LoginPage(driver)
    login_page.login("admin", "admin123")

    def test_login(driver):
        assert "Example" in driver.title
