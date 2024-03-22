import os.path

work_path = "D:/pythonproj/pythonProject/"

class para:
    #原视频时长（秒）
    dur = 0
    #生成ASCII图像数
    num_of_ascii = 0
    #生成PIXEL图像数
    num_of_pixel = 0
    #视频原高
    h = 0
    #视频原宽
    w = 0

class pattern:
    #生成字符串图
    PATTERN_ASCII = 0
    PATTERN_PIXEL = 1

#采样率
sample_rate = 0.4
#字符字体
fonts = "C:/Windows/Fonts/Arial.ttf"
#生成视频帧率
frames = 10


#从原视频截取的所有帧文件夹路径
frames_of_original = "./frames_of_original/"
#转为ASCII形式图片的每一帧文件夹路径
frames_of_ascii = "./frames_of_ascii/"
#原视频素材名称
name_of_original_vedio = "padoru.mp4"
#原视频素材取得帧
frames_of_original = "./frames_of_original/"
#生成的ASCII图像集
frames_of_ascii = "./frames_of_ascii/"
#生成的pixel图像集
frames_of_pixel = "./frames_of_pixel/"
#将要或已有的音频素材名称
name_of_audio = ''+os.path.basename(name_of_original_vedio).split('.')[0]+'.mp3'
#与原视频速度相同的无声像素动画名称
name_of_no_speed_vedio = 'soundless'+os.path.basename(name_of_original_vedio).split('.')[0]+".mp4"
#最终视频
name_of_final_vedio = "final" + os.path.basename(name_of_original_vedio).split('.')[0]+'.mp4'

#点阵模式使用的字符串
pointMatrix = list("⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿⡀⡁⡂⡃⡄⡅⡆⡇⡈⡉⡊⡋⡌⡍⡎⡏⡐⡑⡒⡓⡔⡕⡖⡗⡘⡙⡚⡛⡜⡝⡞⡟⡠⡡⡢⡣⡤⡥⡦⡧⡨⡩⡪⡫⡬⡭⡮⡯⡰⡱⡲⡳⡴⡵⡶⡷⡸⡹⡺⡻⡼⡽⡾⡿⢀⢁⢂⢃⢄⢅⢆⢇⢈⢉⢊⢋⢌⢍⢎⢏⢐⢑⢒⢓⢔⢕⢖⢗⢘⢙⢚⢛⢜⢝⢞⢟⢠⢡⢢⢣⢤⢥⢦⢧⢨⢩⢪⢫⢬⢭⢮⢯⢰⢱⢲⢳⢴⢵⢶⢷⢸⢹⢺⢻⢼⢽⢾⢿⣀⣁⣂⣃⣄⣅⣆⣇⣈⣉⣊⣋⣌⣍⣎⣏⣐⣑⣒⣓⣔⣕⣖⣗⣘⣙⣚⣛⣜⣝⣞⣟⣠⣡⣢⣣⣤⣥⣦⣧⣨⣩⣪⣫⣬⣭⣮⣯⣰⣱⣲⣳⣴⣵⣶⣷⣸⣹⣺⣻⣼⣽⣾⣿")
# 使用字符列表
symbolList = list(" .-+=^!*vMNwxXZzAHIx")

