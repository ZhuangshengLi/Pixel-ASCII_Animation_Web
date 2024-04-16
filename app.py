import os
import time

import globals

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from MAIN import execute

app = Flask(__name__)
cur_video= None

@app.route('/')
def index():
    return render_template('list.html')

@app.route('/upload_video', methods=['POST'])
def uploadvideo():
    if request.method == 'POST':

        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        if file.filename == '':
            return 'No selected file'

        if file:
            upload_folder = '/Users/anthony/PycharmProjects/pythonProject6/Pixel-ASCII_Animation_Web/project'
            filename = secure_filename(file.filename)
            file_path = os.path.join(upload_folder, filename)
            global cur_video
            cur_video = file_path
            file.save(file_path)
            return 'File uploaded successfully'

@app.route('/button_clicked_PIXEL', methods=['POST'])
def button_clicked_PIXEL():
    globals.set_value('PATTERN_ASCII', 0)
    globals.set_value('PATTERN_PIXEL', 1)
    print(f"{cur_video}")
    execute(cur_video)
    return "success"

@app.route('/button_clicked_Ascii', methods=['POST'])
def button_clicked_Ascii():
    globals.set_value('PATTERN_ASCII', 1)
    globals.set_value('PATTERN_PIXEL', 0)
    print(f"{cur_video}")
    execute(cur_video)
    return "success"

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/upload_video_page')
def upload_video_page():
    return render_template('upload_video_page.html')

@app.route('/SamplePage')
def SamplePage():
    return render_template('SamplePage.html')

@app.route('/sample_compare')
def sample_compare():
    return render_template('sample_compare.html')

@app.route('/some_route')
def some_view_function():
    # 假设这是你计算或获取 video_name 的方式
    video_name = 'final_a.mp4'  # 这个值应该根据实际情况动态生成或从请求中获取

    # 确保在调用 render_template 时传递 video_name
    return render_template('upload_video_page.html', video_name=video_name)

# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    app.run()