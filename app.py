from flask import Flask, request, send_file
from gpapi.googleplay import GooglePlayAPI
import io

app = Flask(__name__)

EMAIL = "your_email_here"
PASSWORD = "your_password_here"

@app.route("/")
def home():
    return "APK Downloader API Running 🚀"

@app.route("/download", methods=["POST"])
def download():
    package = request.json.get("package")

    api = GooglePlayAPI(locale="en_US", timezone="UTC")
    api.login(EMAIL, PASSWORD)

    data = api.download(package)
    apk_data = data["file"]["data"]

    return send_file(
        io.BytesIO(apk_data),
        as_attachment=True,
        download_name=f"{package}.apk",
        mimetype="application/vnd.android.package-archive"
    )

app.run(host="0.0.0.0", port=10000)
