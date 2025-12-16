
import os
import subprocess
import tempfile
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    headers = ""
    result = ""
    if request.method == "POST":
        headers = request.form.get("headers", "")
        if headers:
            # Create a temporary file to store the headers
            with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt", encoding='utf-8') as tmp_file:
                tmp_file.write(headers)
                tmp_file_path = tmp_file.name

            try:
                # Run the script as a subprocess
                process = subprocess.run(
                    ["python", "decode-spam-headers.py", tmp_file_path, "-f", "html"],
                    capture_output=True,
                    text=True,
                    encoding='utf-8'
                )
                if process.returncode == 0:
                    result = process.stdout
                else:
                    result = f"Error running script: <pre>{process.stderr}</pre>"
            finally:
                # Clean up the temporary file
                os.remove(tmp_file_path)

    return render_template("index.html", headers=headers, result=result)


