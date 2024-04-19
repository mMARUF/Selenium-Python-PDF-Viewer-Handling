**README**

**Description:**
This Repository utilizes Selenium WebDriver to automate the process of downloading a PDF file from a specified URL. It includes functions to set up the WebDriver, locate and click on the PDF viewer link, verify if the file has been successfully downloaded, and clean up downloaded files after the process is completed.

**Dependencies:**
- Python 3.x
- Selenium WebDriver

**Installation:**
1. Ensure Python is installed on your system.
2. Install Selenium WebDriver using `pip install selenium`.
3. Download and install the appropriate WebDriver for your browser (in this script, Chrome WebDriver is used).
4. Update the `config.ini` file with the URL of the page containing the PDF download link.
5. Update the `path_to_chromedriver` and `download_path` variables in the script to match your system configuration.

**Usage:**
1. Run the script by executing `python script_name.py`.
2. The script will open a Chrome browser, navigate to the specified URL, locate the download link, and click on it to download the PDF file.
3. After the download is completed, the script will verify if the file exists in the specified download path.
4. If the file is found, it will print "File downloaded successfully" along with the file path. Otherwise, it will print "File not found in the specified download path."
5. The script will then delete all files in the specified download path to clean up after the process.

**Note:** Ensure that the download directory (`download_path`) is writable and accessible by the script. Additionally, modify the script as needed to suit your specific use case, such as handling different file names or download scenarios.