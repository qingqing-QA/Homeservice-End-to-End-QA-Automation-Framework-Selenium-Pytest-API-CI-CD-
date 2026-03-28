from pages.login_page import LoginPage

def test_login(driver):
    driver.get("http://localhost/database_javascript/project1/Frontend/index.html")

    login_page = LoginPage(driver)
    login_page.login("admin", "admin123")

    assert "dashboard" in driver.current_url
