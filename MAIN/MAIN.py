import os

from parameterList import *
from function import * #所有操作函数
from command import *

if __name__ == "__main__":

    # os.system("ffmpeg -i " + ascii_output_path + "%04d.jpg.ascii.png" " -c:v libx264 -vf fps=" + str(frames) + " -pix_fmt yuv420p " + video_output_path)

    # os.system("ffmpeg -i D:/pythonproj/pythonProject/vedio.mp4 -an -r 60 -filter:v \"setpts=2.0*PTS\" D:/pythonproj/pythonProject/normal_vedio.mp4")


    #切换到项目目录
    changeToProjectFold()

    #生成帧的暂存目录
    foldGenerate()

    #获取视频宽高
    get_size()

    '''#视频分帧
    getFrames()

    all_file = os.listdir(frames_of_original)
    if(pattern.PATTERN_ASCII == 1):

       process = [img2ASCIImg(frames_of_original + x) for x in all_file if x.endswith('.png') or x.endswith('.jpg')]
       # 计算ascii图像的数量
       para.num_of_ascii = num_of_file(frames_of_ascii)

    elif(pattern.PATTERN_PIXEL == 1):

       process = [img2PIXImg(frames_of_original + x) for x in all_file if x.endswith('.png') or x.endswith('.jpg')]
       # 计算ascii图像的数量
       para.num_of_pixel = num_of_file(frames_of_pixel)'''


    #获取视频时长
    para.num_of_pixel = num_of_file(frames_of_pixel)
    get_dur()

    #视频合帧及调速
    integrate()

    #获取音频
    getAudio()

    #视频音频合流
    merge()








