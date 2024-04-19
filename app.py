import os

import globals

from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from MAIN import execute

app = Flask(__name__)
cur_video= None
global processing_status
processing_status = False

@app.route('/')
def index():
    return render_template('index.html')

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
    global processing_status
    globals.set_value('PATTERN_ASCII', 0)
    globals.set_value('PATTERN_PIXEL', 1)
    print(f"{cur_video}")
    execute(cur_video)
    processing_status = True
    return "convert PIXEL success"

@app.route('/button_clicked_Ascii', methods=['POST'])
def button_clicked_Ascii():
    global processing_status
    globals.set_value('PATTERN_ASCII', 1)
    globals.set_value('PATTERN_PIXEL', 0)
    print(f"{cur_video}")
    execute(cur_video)
    processing_status = True
    return "convert Ascii success"

@app.route('/history')
def history():
    return render_template('history_sample.html')

@app.route('/upload')
def upload():
    return render_template('upload_video_page.html')

# @app.route('/upload_video_page')
# def upload_video_page():
#     return render_template('upload_video_page.html')

@app.route('/SamplePage')
def SamplePage():
    return render_template('SamplePage.html')

@app.route('/status/<filename>', methods=['GET'])
def check_status(filename):
    global processing_status
    status = processing_status
    if status == False:
        return jsonify({'status': 'processing'})
    else:
        return jsonify({'status': 'processed', 'url': f'./static/video/final_{filename}.mp4'})

@app.route('/video_play', methods=['GET'])
def video_play():
    if cur_video:
        video_name = f"final_{cur_video.split('/')[-1]}"
    # video_name = 'final_22.mp4'
    print('cur_video', cur_video)
    # /Users/anthony/PycharmProjects/pythonProject6/Pixel-ASCII_Animation_Web/project/22.mp4
    return render_template('video_playn.html', video_name = video_name)

# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    app.run()