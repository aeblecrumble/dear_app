from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# アップロードフォルダの設定
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ルートページを表示
@app.route('/')
def index():
    return render_template('index.html')

# 写真アップロード処理
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return f"File uploaded successfully: {file.filename}"

if __name__ == '__main__':
    app.run(debug=True)
