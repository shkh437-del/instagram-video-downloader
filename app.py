from flask import Flask, request, jsonify
import instaloader

app = Flask(__name__)

@app.route("/")
def home():
    return "Instagram Downloader API is running"

@app.route("/download")
def download():
    url = request.args.get("url", "")
    if "instagram.com" not in url:
        return jsonify({"error": "Invalid URL"}), 400
    return jsonify({"message": "URL received", "url": url})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
