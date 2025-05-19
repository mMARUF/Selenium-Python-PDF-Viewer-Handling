import os
import time

def is_file_downloaded(download_path, file_name, timeout=30):
    """
    Wait up to `timeout` seconds for the file to appear in the download path.
    Returns True if found, False otherwise.
    """
    file_path = os.path.join(download_path, file_name)
    waited = 0
    while waited < timeout:
        if os.path.exists(file_path):
            return True
        time.sleep(1)
        waited += 1
    return False

def delete_files_in_folder(folder_path):
    """
    Deletes all files in the specified folder.
    Returns a list of deleted file paths.
    """
    deleted_files = []
    if not os.path.exists(folder_path):
        return deleted_files
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
            deleted_files.append(file_path)
    return deleted_files