from selenium.webdriver.common.by import By

class DownloadPage:
    DOWNLOAD_LINK = (By.LINK_TEXT, "Download a Printable PDF of this Cheat Sheet")
    DOWNLOAD_BUTTON_LOCATOR = (By.LINK_TEXT, "Download a Printable PDF of this Cheat Sheet")    

    def __init__(self, driver):
        self.driver = driver

    def is_download_button_visible(self):
        try:
            button = self.driver.find_element(*self.DOWNLOAD_BUTTON_LOCATOR)
            return button.is_displayed()
        except Exception:
            return False    

    def open(self, url):
        self.driver.get(url)

    def click_download(self):
        link = self.driver.find_element(*self.DOWNLOAD_LINK)
        assert link.is_displayed()
        link.click()