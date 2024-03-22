from PIL import Image, ImageDraw, ImageFont
from parameterList import * #所有参数
import numpy as np
import cv2 as cv
import os


'''-------------------辅助功能--------------------------'''

def foldGenerate():      #生成帧的暂存目录
    if not os.path.exists("./frames_of_original"):
        os.mkdir("./frames_of_original")
    if not os.path.exists("./frames_of_ascii"):
        os.mkdir("./frames_of_ascii")
    if not os.path.exists("./frames_of_pixel"):
        os.mkdir("./frames_of_pixel")

def get_dur():   #计算视频时长
    cap = cv.VideoCapture(name_of_original_vedio)
    fps = int(round(cap.get(cv.CAP_PROP_FPS)))
    frame_counter = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

    cap.release()
    # 时长，单位s
    para.dur = frame_counter / fps


def get_size():     #获取视频宽高
    cap = cv.VideoCapture(name_of_original_vedio)
    para.h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    para.w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))


def num_of_file(path):  #计算文件夹内照片数
    files = os.listdir(path)
    num_pic = len(files)
    return num_pic


'''----------------------生成算法--------------------------------'''

def img2PIXImg(filename, new_width=2048, new_height=2048, pixel_size=20):
    img = Image.open(filename)
    img = img.resize([new_width, new_height], Image.NEAREST)
    img_new = Image.new('RGB', (new_width, new_height), "black")
    draw = ImageDraw.Draw(img_new)

    for y in range(new_height // pixel_size):
        for x in range(0, new_width // pixel_size):
            print(str(x) + "---" + str(y))
            block = np.array(img.crop((x * pixel_size,
                                       y * pixel_size,
                                       x * pixel_size + pixel_size,
                                       y * pixel_size + pixel_size)))
            avg_color = tuple(np.mean(block.reshape(-1, 3), axis=0).astype(np.uint8))
            draw.rectangle([x * pixel_size, y * pixel_size, (x + 1) * pixel_size, (y + 1) * pixel_size], fill=avg_color)

    img_new.save(os.path.join(work_path + "frames_of_pixel/" + os.path.basename(filename)))

def img2ASCIImg(filename, new_width=para.w, new_height=para.h, font_size=10, symbols=np.array(symbolList)):
    ascii_chars = symbols
    img = Image.open(filename)
    img = img.resize([new_width, new_height])
    img_color_pick = img
    w, h = img.size
    img = img.convert("L").resize((new_width, int(new_width*h//w)))

    w, h = img.size
    data = img.load()
    img_new = Image.new('RGB', (w, h), "black")
    f = ImageFont.truetype('arial.ttf', font_size)
    d = ImageDraw.Draw(img_new)
    n = len(ascii_chars)-1

    for y in range(h//font_size):
        for x in range(w//font_size):
            print(str(x) + "---" + str(y))
            char = ascii_chars[data[x*font_size, y*font_size]*n//255]
            color = img_color_pick.getpixel((x*font_size, y*font_size))
            d.text((x*font_size, y*font_size), char, color, font=f)

    # Save image file
    img_new.save(os.path.join(work_path + "frames_of_ascii/" + os.path.basename(filename)))



'''---------------------------参数获取------------------------------'''