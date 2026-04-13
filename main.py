import re
import sys
from gpapi.googleplay import GooglePlayAPI


def extract_package_name(playstore_url):
    match = re.search(r"id=([a-zA-Z0-9._]+)", playstore_url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid Play Store URL")


def login(api, email, password):
    print("[*] Logging in...")
    api.login(email, password)
    print("[+] Login successful")


def download_apk(api, package_name):
    print(f"[*] Fetching APK for: {package_name}")
    
    try:
        data = api.download(package_name)
        apk_bytes = data["file"]["data"]

        file_name = f"{package_name}.apk"
        with open(file_name, "wb") as f:
            f.write(apk_bytes)

        print(f"[+] APK saved as {file_name}")

    except Exception as e:
        print(f"[!] Error: {e}")


def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <playstore_url> <email> <password>")
        return

    url = sys.argv[1]
    email = sys.argv[2]
    password = sys.argv[3]

    try:
        package_name = extract_package_name(url)
        print(f"[+] Package Name: {package_name}")

        api = GooglePlayAPI(locale="en_US", timezone="UTC")

        login(api, email, password)
        download_apk(api, package_name)

    except Exception as e:
        print(f"[!] Failed: {e}")


if __name__ == "__main__":
    main()
