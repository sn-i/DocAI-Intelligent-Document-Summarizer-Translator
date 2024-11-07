from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['files']
    from_lang = request.files['from_lang']
    to_lang = request.files['to_lang']

    if file.filename == '':
        return 'No selected file'

    return f"File: {file.filename}, from: {from_lang}, To: {to_lang}"


if __name__ == "__main__":
    app.run(debug=True)
