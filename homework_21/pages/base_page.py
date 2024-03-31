from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def find(self, args):
        return self.browser.find_element(*args)

    @property
    def is_displayed(self):
        return self.browser.is_displayed()

    def text(self):
        return self.browser.text()

    def send_keys(self, args):
        return self.browser.send_keys(args)

    def click(self):
        return self.browser.click()

    def is_enabled(self):
        return self.browser.is_enabled()

    def script_click(self, element):
        return self.browser.execute_script("arguments[0].click();", element)

    def save_screenshot(self, file_name: str):
        return self.browser.save_screenshot(f"screenshots/{file_name}.png")

    def visibility_of_element_located(self, locator):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))

