import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import configparser
import os

@pytest.fixture(scope="session")
def config():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
    return config

@pytest.fixture
def browser(config):
    driver_path = config["Settings"].get("chromedriver_path", "drivers/chromedriver")
    download_dir = config["Settings"].get("download_dir", os.path.expanduser("~/Downloads/downloaded_pdf"))

    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "plugins.always_open_pdf_externally": True,
        "download.default_directory": download_dir
    }
    chrome_options.add_experimental_option("prefs", prefs)
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            screenshot_path = os.path.join(os.getcwd(), "screenshot_{}.png".format(item.name))
            driver.save_screenshot(screenshot_path)
            if hasattr(rep, "extra"):
                rep.extra.append(pytest_html.extras.png(screenshot_path))