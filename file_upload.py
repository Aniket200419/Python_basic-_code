from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]

    # Get original extension
    extension = os.path.splitext(file.filename)[1]

    # New file name
    new_filename = "file1" + extension

    file.save(os.path.join(UPLOAD_FOLDER, new_filename))

    return f"Saved as {new_filename}"

if __name__ == "__main__":
    app.run(debug=True)