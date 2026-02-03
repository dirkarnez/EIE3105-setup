import urllib.request
import os

def download_file_urllib(url, filename):
    """Downloads a file from a URL using urllib.request.urlretrieve."""
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Downloaded successfully to {os.path.abspath(filename)}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
download_file_urllib("http://example.com/path/to/your/file.zip", "local_filename.zip")

import zipfile
import os

def unzip_file_zipfile(zip_filename, extract_dir='.'):
    """
    Extracts all contents of a zip file to a specified directory using the zipfile module.

    Args:
        zip_filename (str): The path to the zip file.
        extract_dir (str, optional): The destination directory. Defaults to the current directory.
    """
    # Create the destination directory if it doesn't exist
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)

    # Open the zip file in read mode using a context manager
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        # Extract all files to the specified directory
        zip_ref.extractall(extract_dir)
        print(f"Extracted all files from '{zip_filename}' to '{extract_dir}'")

# Example usage:
# unzip_file_zipfile('my_archive.zip', 'extracted_folder')
