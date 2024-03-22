from parameterList import *
import os

#切换到项目目录

def changeToProjectFold():
    os.system("cd " + work_path)

#视频分帧
def getFrames():
    os.system("ffmpeg -i " +
               name_of_original_vedio +
               " -f image2" +
               " -vf fps=fps=" +
               str(frames) +
               " -qscale:v 2 " +
               frames_of_original +
               "%05d.png"
               )

#视频合帧及调速
def integrate():
    if(pattern.PATTERN_ASCII == 1):
        os.system("ffmpeg -framerate " +
                  str(round(1/(para.dur/para.num_of_ascii), 2)) +
                  " -f image2 -loop 1 -i " +
                  frames_of_ascii +
                  "%05d.png" +
                  " -vcodec libx264 -pix_fmt yuv420p -s " + str(para.w) + "*" + str(para.h) + " -r " +
                  str(frames) +
                  " -t " +
                  str(para.dur) +
                  " -y " +
                  name_of_no_speed_vedio
                  )
    elif (pattern.PATTERN_PIXEL == 1):
        os.system("ffmpeg -framerate " +
                  str(round(1/(para.dur/para.num_of_pixel), 2)) +
                  " -f image2 -loop 1 -i " +
                  frames_of_pixel +
                  "%05d.png" +
                  " -vcodec libx264 -pix_fmt yuv420p -s " + str(para.w) + "*" + str(para.h) + " -r " +
                  str(frames) +
                  " -t " +
                  str(para.dur) +
                  " -y " +
                  name_of_no_speed_vedio
                  )

#获取音频
def getAudio():
    os.system(
              "ffmpeg -i " +
              name_of_original_vedio +
              " -c:a libmp3lame -q:a 2 " +
              name_of_audio
             )


#视频音频合流
def merge():
    os.system(
              "ffmpeg -i " +
              name_of_no_speed_vedio +
              " -i " +
              name_of_audio +
              " -c:v copy -map 0:v -map 1:a " +
              name_of_final_vedio
             )