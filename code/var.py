import globals
import os.path


def init():
    globals.set_value('work_path', 'D:/pythonproj/pythonProject/')

    # 原视频时长（秒）
    globals.set_value('dur', 0)
    # 生成ASCII图像数
    globals.set_value('num_of_ascii', 0)
    # 生成PIXEL图像数
    globals.set_value('num_of_pixel', 0)
    # 视频宽
    globals.set_value('wide', 0)
    # 视频高
    globals.set_value('high', 0)

    # 生成字符串图标识
    globals.set_value('PATTERN_ASCII', 0)
    # 生成像素图标识
    globals.set_value('PATTERN_PIXEL', 1)

    # 采样率
    globals.set_value('sample_rate', 0.4)
    # 字符字体
    globals.set_value('fonts', 'C:/Windows/Fonts/Arial.ttf')
    # 生成视频帧率
    globals.set_value('frames', 10)

    # 单个请求的输入和输出
    globals.set_value('project_folder', './project/')
    # 从原视频截取的所有帧文件夹路径
    globals.set_value('frames_of_original', './project/frames_of_original/')
    # 原视频素材名称
    globals.set_value('name_of_original_video', './project/heita.mp4')
    # 转为ASCII形式图片的每一帧文件夹路径
    globals.set_value('frames_of_ascii', './project/frames_of_ascii/')
    # 生成的pixel图像集
    globals.set_value('frames_of_pixel', './project/frames_of_pixel/')
    # 将要或已有的音频素材名称
    name_of_audio = globals.get_value('project_folder') + os.path.basename(globals.get_value('name_of_original_video')).split('.')[0] + '.mp3'
    globals.set_value('name_of_audio', name_of_audio)
    # 与原视频速度相同的无声像素动画名称
    soundless_video = globals.get_value('project_folder') + 'soundless_' + os.path.basename(globals.get_value('name_of_original_video')).split('.')[
        0] + '.mp4'
    globals.set_value('soundless_video', soundless_video)
    # 最终视频
    final_video = globals.get_value('project_folder') + 'final_' + os.path.basename(globals.get_value('name_of_original_video')).split('.')[0] + '.mp4'
    globals.set_value('final_video', final_video)

    # 点阵模式使用的字符串
    # pointMatrix = list('⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿⡀⡁⡂⡃⡄⡅⡆⡇⡈⡉⡊⡋⡌⡍⡎⡏⡐⡑⡒⡓⡔⡕⡖⡗⡘⡙⡚⡛⡜⡝⡞⡟⡠⡡⡢⡣⡤⡥⡦⡧⡨⡩⡪⡫⡬⡭⡮⡯⡰⡱⡲⡳⡴⡵⡶⡷⡸⡹⡺⡻⡼⡽⡾⡿⢀⢁⢂⢃⢄⢅⢆⢇⢈⢉⢊⢋⢌⢍⢎⢏⢐⢑⢒⢓⢔⢕⢖⢗⢘⢙⢚⢛⢜⢝⢞⢟⢠⢡⢢⢣⢤⢥⢦⢧⢨⢩⢪⢫⢬⢭⢮⢯⢰⢱⢲⢳⢴⢵⢶⢷⢸⢹⢺⢻⢼⢽⢾⢿⣀⣁⣂⣃⣄⣅⣆⣇⣈⣉⣊⣋⣌⣍⣎⣏⣐⣑⣒⣓⣔⣕⣖⣗⣘⣙⣚⣛⣜⣝⣞⣟⣠⣡⣢⣣⣤⣥⣦⣧⣨⣩⣪⣫⣬⣭⣮⣯⣰⣱⣲⣳⣴⣵⣶⣷⣸⣹⣺⣻⣼⣽⣾⣿')
    # 使用字符列表
    symbolList = ' .-+=^!*vMNwxXZzAHIx'
    globals.set_value('symbolList', symbolList)
