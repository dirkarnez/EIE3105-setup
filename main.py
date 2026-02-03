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
