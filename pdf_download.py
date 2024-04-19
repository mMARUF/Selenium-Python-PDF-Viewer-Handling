from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import configparser
import os
import pathlib
import time





# Read the URL from config file
config = configparser.ConfigParser()
config.read('config.ini')
url = config['Settings']['url']

def get_browser():
    
    path_to_chromedriver = '/Users/user_name/Downloads/pdf-download-selenium/node_modules/chromedriver/bin/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    prefs = {"plugins.always_open_pdf_externally": True, "download.default_directory": '/Users/user_name/Desktop/downloaded_pdf/'}
    chrome_options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(executable_path=path_to_chromedriver,
                               chrome_options=chrome_options)
    return browser   


def download_file_example(browser):
    browser.get(url);
    signin_link = browser.find_element(By.LINK_TEXT, "Download a Printable PDF of this Cheat Sheet")

    # Assert that a certain element is visible on the page
    assert signin_link.is_displayed()


    signin_link.click()

    

browser = get_browser()
download_file_example(browser)


def is_file_downloaded(download_path, file_name):
    # Check if the file exists in the download path
    file_path = os.path.join(download_path, file_name)
    return os.path.exists(file_path)

# Example usage
download_path = "/Users/user_name/Desktop/downloaded_pdf/"  # Specify your download path here
file_name = "Selenium-Cheat-Sheet-2022.pdf"  # Specify the name of the downloaded file here    

# Check if the file is downloaded
time.sleep(5);
if is_file_downloaded(download_path, file_name):
    print("File downloaded successfully at:", os.path.join(download_path, file_name))
else:
    print("File not found in the specified download path.")

# Specify the path of the folder containing the files you want to delete
folder_path = '/Users/user_name/Desktop/downloaded_pdf/'

# Get a list of all files in the folder
file_list = os.listdir(folder_path)

# Iterate over each file and delete it
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        os.remove(file_path)
        print("Deleted file: {}".format(file_path))
    else:
        print("Could not delete file: {}".format(file_path))
        


time.sleep(5);
browser.quit()
