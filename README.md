# Selenium-Python-PDF-Viewer-Handling

## Description

This repository utilizes Selenium WebDriver and pytest to automate the process of downloading a PDF file from a specified URL. It includes functions to set up the WebDriver, locate and click on the PDF download link, verify if the file has been successfully downloaded, and clean up downloaded files after the process is completed. The project also features robust assertions and generates detailed HTML test reports.

---

## Project Structure

```
Selenium-Python-PDF-Viewer-Handling/
├── pages/
│   └── download_page.py
├── tests/
│   └── pdf_test.py
├── drivers/
│   └── chromedriver
├── .venv/
├── config.ini
├── conftest.py
├── requirements.txt
├── pytest.ini
├── README.md
```

---

## Dependencies

- Python 3.x
- Selenium (`pip install selenium`)
- pytest (`pip install pytest`)
- pytest-html (`pip install pytest-html`)
- configparser (usually included with Python)
- Chrome WebDriver (or another browser driver as needed)

---

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd Selenium-Python-PDF-Viewer-Handling
    ```

2. **Set up a virtual environment (recommended):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download and place the appropriate WebDriver (e.g., chromedriver) in the `drivers/` directory.**

5. **Update the `config.ini` file with:**
    - The URL of the page containing the PDF download link.
    - The path to your chromedriver.
    - The download directory and file name.

    Example:
    ```
    [Settings]
    url = https://your-url.com/path/to/pdf
    chromedriver_path = drivers/chromedriver
    download_dir = /Users/youruser/Downloads/downloaded_pdf
    file_name = your_file.pdf
    ```

---

## Usage

1. **Run the tests and generate an HTML report:**
    ```bash
    pytest --html=report.html
    ```

2. **Open `report.html` in your browser to view the test results and screenshots for any failed tests.**

---

## Reporting

- **pytest-html** is used for generating HTML test reports.
- Screenshots are automatically captured and attached to the report for failed Selenium tests.

---

## Assertions

The test suite includes assertions to ensure:
- The browser navigates to the correct URL.
- The download button is visible before clicking.
- The download link is clicked.
- The PDF file is successfully downloaded and present in the specified folder.
- The downloaded file is deleted after the test, and its absence is verified.

---

## Required Libraries

All required libraries are listed in `requirements.txt`.  
Install them with:
```bash
pip install -r requirements.txt
```

---

## Notes

- Ensure that the download directory (`download_dir`) is writable and accessible by the script.
- Modify the script as needed to suit your specific use case, such as handling different file names or download scenarios.
- For Firefox or other browsers, update the WebDriver and options accordingly.

---