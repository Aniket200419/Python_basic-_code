
import os
import urllib.request
import urllib.parse

def download_file():
    print("=" * 45)
    print("       PYTHON FILE DOWNLOADER")
    print("=" * 45)

    url = input("Enter file download URL: ").strip()

    if not url.startswith(("http://", "https://")):
        print("Error: Please enter a valid HTTP or HTTPS URL.")
        return

    try:
        # Extract filename from URL
        filename = os.path.basename(
            urllib.parse.urlparse(url).path
        )

        if not filename:
            filename = input("Enter filename to save: ").strip()

        if not filename:
            print("Error: Filename cannot be empty.")
            return

        # Save file in Downloads folder
        download_folder = os.path.join(
            os.path.expanduser("~"), "Downloads"
        )

        os.makedirs(download_folder, exist_ok=True)

        file_path = os.path.join(download_folder, filename)

        print("\nDownloading...")

        urllib.request.urlretrieve(url, file_path)

        print("\nFile downloaded successfully!")
        print("Saved location:", file_path)

    except Exception as e:
        print("\nDownload failed:", e)


if __name__ == "__main__":
    download_file()
