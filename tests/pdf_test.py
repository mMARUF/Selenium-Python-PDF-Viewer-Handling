import os
import time
from pages.download_page import DownloadPage

def is_file_downloaded(download_path, file_name, timeout=10):
    file_path = os.path.join(download_path, file_name)
    for _ in range(timeout):
        if os.path.exists(file_path):
            return True
        time.sleep(1)
    return False

def remove_file_if_exists(download_path, file_name):
    file_path = os.path.join(download_path, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)

def test_pdf_download(browser, config):
    url = config['Settings']['url']
    download_path = config['Settings']['download_path']
    file_name = config['Settings']['file_name']

    remove_file_if_exists(download_path, file_name)

    page = DownloadPage(browser)
    page.open(url)
    assert browser.current_url == url, "Did not navigate to the correct URL"
    assert page.is_download_button_visible(), "Download button not visible"

    page.click_download()
    assert is_file_downloaded(download_path, file_name), "PDF was not downloaded."
    assert os.path.exists(os.path.join(download_path, file_name)), "Downloaded file not found in folder."    

    remove_file_if_exists(download_path, file_name)
    assert not os.path.exists(os.path.join(download_path, file_name)), "Downloaded file was not deleted."    