import var
from command import *
from function import *  # 所有操作函数
import globals

def execute(path):
    # globals.init()
    var.init(path)

    # 切换到项目目录
    changeToProjectFold()

    # 生成帧的暂存目录
    foldGenerate()

    # 获取视频宽高
    get_size()

    # 视频分帧
    getFrames()

    all_file = os.listdir(globals.get_value('frames_of_original'))

    if (globals.get_value('PATTERN_ASCII')):

        process = [img2ASCIImg(globals.get_value('frames_of_original') + x, globals.get_value('size')) for x in all_file if
                   x.endswith('.png') or x.endswith('.jpg')]
        # 计算ascii图像的数量
        num_of_ascii = num_of_file(globals.get_value('frames_of_ascii'))
        globals.set_value('num_of_ascii', num_of_ascii)

    elif (globals.get_value('PATTERN_PIXEL')):

        process = [img2PIXImg(globals.get_value('frames_of_original') + x, globals.get_value('size')) for x in all_file if
                   x.endswith('.png') or x.endswith('.jpg')]
        # 计算ascii图像的数量
        num_of_pixel = num_of_file(globals.get_value('frames_of_pixel'))
        globals.set_value('num_of_pixel', num_of_pixel)

    # 获取视频时长
    get_dur()

    # 视频合帧及调速
    integrate()

    # 获取音频
    getAudio()

    # 视频音频合流
    merge()
