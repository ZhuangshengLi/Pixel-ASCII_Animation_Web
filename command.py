import os
from var import *



# 切换到项目目录

def changeToProjectFold():
    os.system("cd " + globals.get_value('work_path'))
    if not os.path.exists(globals.get_value('project_folder')):
        os.mkdir(globals.get_value('project_folder'))


# 视频分帧
def getFrames():
    os.system("ffmpeg -i " +
              globals.get_value('name_of_original_video') +
              " -f image2" +
              " -vf fps=fps=" +
              str(globals.get_value('frames')) +
              " -qscale:v 2 " +
              globals.get_value('frames_of_original') +
              "%05d.png"
              )


# 视频合帧及调速
def integrate():
    if (globals.get_value('PATTERN_ASCII')):
        os.system("ffmpeg -framerate " +
                  str(round(1 / (globals.get_value('dur') / globals.get_value('num_of_ascii')), 2)) +
                  " -f image2 -loop 1 -i " +
                  globals.get_value('frames_of_ascii') +
                  "%05d.png" +
                  " -vcodec libx264 -pix_fmt yuv420p -s " + str(globals.get_value('wide')) + "*" + str(
            globals.get_value('high')) + " -r " +
                  str(globals.get_value('frames')) +
                  " -t " +
                  str(globals.get_value('dur')) +
                  " -y " +
                  globals.get_value('soundless_video')
                  )
    elif (globals.get_value('PATTERN_PIXEL')):
        os.system("ffmpeg -framerate " +
                  str(round(1 / (globals.get_value('dur') / globals.get_value('num_of_pixel')), 2)) +
                  " -f image2 -loop 1 -i " +
                  globals.get_value('frames_of_pixel') +
                  "%05d.png" +
                  " -vcodec libx264 -pix_fmt yuv420p -s " + str(globals.get_value('wide')) + "*" + str(
            globals.get_value('high')) + " -r " +
                  str(globals.get_value('frames')) +
                  " -t " +
                  str(globals.get_value('dur')) +
                  " -y " +
                  globals.get_value('soundless_video')
                  )


# 获取音频
def getAudio():
    os.system(
        "ffmpeg -i " +
        globals.get_value('name_of_original_video') +
        " -c:a libmp3lame -q:a 2 " +
        globals.get_value('name_of_audio')
    )



# 视频音频合流
def merge():
    os.system(
        "ffmpeg -i " +
        globals.get_value('soundless_video') +
        " -i " +
        globals.get_value('name_of_audio') +
        " -c:v copy -map 0:v -map 1:a " +
        globals.get_value('final_video')
    )
