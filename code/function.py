from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import globals
import numpy as np
import cv2 as cv
import os

'''-------------------辅助功能--------------------------'''


def foldGenerate():  # 生成帧的暂存目录
    if not os.path.exists(globals.get_value('frames_of_original')):
        os.mkdir(globals.get_value('frames_of_original'))
    if not os.path.exists(globals.get_value('frames_of_ascii')):
        os.mkdir(globals.get_value('frames_of_ascii'))
    if not os.path.exists(globals.get_value('frames_of_pixel')):
        os.mkdir(globals.get_value('frames_of_pixel'))


def get_dur():  # 计算视频时长
    cap = cv.VideoCapture(globals.get_value('name_of_original_video'))
    fps = int(round(cap.get(cv.CAP_PROP_FPS)))
    frame_counter = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

    cap.release()
    # 时长，单位s
    globals.set_value('dur', frame_counter / fps)


def get_size():  # 获取视频宽高
    cap = cv.VideoCapture(globals.get_value('name_of_original_video'))
    globals.set_value('high', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
    globals.set_value('wide', int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))


def num_of_file(path):  # 计算文件夹内照片数
    files = os.listdir(path)
    num_pic = len(files)
    return num_pic


'''----------------------生成算法--------------------------------'''


def img2PIXImg(filename, size=None, pixel_size=8):
    if size is None:
        size = [globals.get_value('wide'), globals.get_value('high')]
    img = Image.open(filename)
    img = img.resize(size, Image.NEAREST)
    img_new = Image.new('RGB', (size[0], size[1]), "black")
    draw = ImageDraw.Draw(img_new)

    for y in range(size[1] // pixel_size):
        for x in range(size[0] // pixel_size):
            print(str(x) + "---" + str(y))
            block = np.array(img.crop((x * pixel_size,
                                       y * pixel_size,
                                       x * pixel_size + pixel_size,
                                       y * pixel_size + pixel_size)))
            avg_color = tuple(np.mean(block.reshape(-1, 3), axis=0).astype(np.uint8))

            gray_value = (128, 128, 128)

            color = tuple(max(0, component - 30) for component in avg_color) \
                if all(component < g for component, g in zip(avg_color, gray_value)) \
                else avg_color

            draw.rectangle([x * pixel_size, y * pixel_size, (x + 1) * pixel_size, (y + 1) * pixel_size], fill=color)

    img_new = sharpen(img_new)

    img_new.save(os.path.join(globals.get_value('frames_of_pixel') + os.path.basename(filename)))


def img2ASCIImg(filename, size=None, font_size=10, symbols=np.array(list(' .-+=^EB*vMNwxXZzAHK')), enhance_factor=1.5,
                constract_factor=1.5):
    if size is None:
        size = [globals.get_value('wide'), globals.get_value('high')]
    ascii_chars = symbols

    img = Image.open(filename)
    sharpen_img = img.filter(ImageFilter.SHARPEN)
    img = sharpen_img
    '''
    # 获取边界
    edge = getEdge(filename)

    # 图像饱和度对比度增强
    enhancer = ImageEnhance.Color(img).enhance(enhance_factor)
    constracter = ImageEnhance.Contrast(enhancer).enhance(constract_factor)

    # 图像描边
    img = Image.blend(constracter, edge, 0.5)'''

    img = img.resize(size)
    img_color_pick = img
    w, h = img.size
    img = img.convert("L").resize((size[0], int(size[0] * h // w)))

    w, h = img.size
    data = img.load()
    img_new = Image.new('RGB', (w, h), "white")
    f = ImageFont.truetype('arial.ttf', font_size)
    d = ImageDraw.Draw(img_new)
    n = len(ascii_chars) - 1
    space = font_size - 2

    for y in range(h // space):
        for x in range(w // space):
            print(str(x) + "---" + str(y))
            char = ascii_chars[data[x * space, y * space] * n // 255]
            color = img_color_pick.getpixel((x * space, y * space))

            d.text((x * space, y * space), char, color, font=f)

    # Save image file
    img_new.save(os.path.join(globals.get_value('frames_of_ascii') + os.path.basename(filename)))


def sharpen(image):
    src = cv.cvtColor(np.asarray(image), cv.COLOR_RGB2BGR)

    # sigma = 5、15、25
    blur_img = cv.GaussianBlur(src, (0, 0), 25)
    usm = cv.addWeighted(src, 1.5, blur_img, -0.5, 0)
    # cv.addWeighted(图1,权重1, 图2, 权重2, gamma修正系数, dst可选参数, dtype可选参数)

    h, w = src.shape[:2]
    result = np.zeros([h, w * 2, 3], dtype=src.dtype)
    result[0:h, 0:w, :] = src
    result[0:h, w:2 * w, :] = usm

    result = Image.fromarray(cv.cvtColor(src, cv.COLOR_BGR2RGB))

    return result


def shapen_Laplacian(image):
    img = cv.cvtColor(np.asarray(image), cv.COLOR_RGB2BGR)
    I = img.copy()
    L = cv.Canny(img, 50, 100)
    e = cv.cvtColor(L, cv.COLOR_GRAY2BGR)
    O = cv.addWeighted(I, 1, e, 0.5, 0)
    O[O > 255] = 255
    O[O < 0] = 0

    image = Image.fromarray(cv.cvtColor(O, cv.COLOR_BGR2RGB))
    return image


'''---------------------------参数获取------------------------------'''
