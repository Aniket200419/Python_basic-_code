
from flask import Flask, request, render_template_string, send_from_directory
from werkzeug.utils import secure_filename
from pathlib import Path

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)

app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024  # 20 MB

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Python File Upload System</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f1f5f9;
            margin: 0;
            padding: 30px 15px;
        }
        .container {
            max-width: 650px;
            margin: auto;
            background: white;
            padding: 25px;
            border-radius: 14px;
            box-shadow: 0 4px 18px #0001;
        }
        h1 { color: #2563eb; text-align: center; }
        .upload-box {
            border: 2px dashed #2563eb;
            border-radius: 10px;
            padding: 25px;
            text-align: center;
        }
        input { margin: 15px 0; max-width: 100%; }
        button {
            background: #2563eb;
            color: white;
            border: 0;
            padding: 12px 22px;
            border-radius: 7px;
            cursor: pointer;
        }
        .message { color: #15803d; margin: 15px 0; }
        .error { color: #dc2626; }
        li { margin: 12px 0; overflow-wrap: anywhere; }
        a { color: #2563eb; }
    </style>
</head>
<body>
<div class="container">
    <h1>Python File Upload</h1>
    <p>Upload your files securely using this simple web application.</p>

    {% if message %}
        <p class="{{ 'error' if error else 'message' }}">{{ message }}</p>
    {% endif %}

    <form method="POST" enctype="multipart/form-data">
        <div class="upload-box">
            <h3>Select a file</h3>
            <input type="file" name="file" required>
            <br>
            <button type="submit">Upload File</button>
            <p>Maximum file size: 20 MB</p>
        </div>
    </form>

    <h2>Uploaded Files</h2>
    {% if files %}
        <ul>
        {% for filename in files %}
            <li>
                {{ filename }}
                — <a href="{{ url_for('download_file', filename=filename) }}">
                    Download
                  </a>
            </li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No files uploaded yet.</p>
    {% endif %}
</div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    error = False

    if request.method == "POST":
        uploaded_file = request.files.get("file")

        if not uploaded_file or not uploaded_file.filename:
            message = "Please select a file."
            error = True
        else:
            filename = secure_filename(uploaded_file.filename)

            if not filename:
                message = "Invalid filename."
                error = True
            else:
                destination = UPLOAD_FOLDER / filename

                try:
                    uploaded_file.save(destination)
                    message = f"File '{filename}' uploaded successfully!"
                except OSError:
                    message = "Unable to save the file."
                    error = True

    files = sorted(p.name for p in UPLOAD_FOLDER.iterdir() if p.is_file())

    return render_template_string(
        HTML, files=files, message=message, error=error
    )


@app.route("/download/<path:filename>")
def download_file(filename):
    return send_from_directory(
        UPLOAD_FOLDER, filename, as_attachment=True
    )


@app.errorhandler(413)
def file_too_large(error):
    files = sorted(p.name for p in UPLOAD_FOLDER.iterdir() if p.is_file())
    return render_template_string(
        HTML,
        files=files,
        message="File is too large. Maximum allowed size is 20 MB.",
        error=True,
    ), 413


if __name__ == "__main__":
    app.run(debug=True)
