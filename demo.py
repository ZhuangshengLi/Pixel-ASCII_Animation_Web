import os

try:
    for filename in os.listdir("project/frames_of_pixel"):
        file_path = os.path.join("project/frames_of_pixel", filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # 删除文件或链接
            elif os.path.isdir(file_path):
                os.rmdir(file_path)  # 删除空文件夹
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

    for filename in os.listdir("project/frames_of_original"):
        file_path = os.path.join("project/frames_of_original", filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # 删除文件或链接
            elif os.path.isdir(file_path):
                os.rmdir(file_path)  # 删除空文件夹
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

    for filename in os.listdir("project/frames_of_ascii"):
        file_path = os.path.join("project/frames_of_ascii", filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # 删除文件或链接
            elif os.path.isdir(file_path):
                os.rmdir(file_path)  # 删除空文件夹
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
    print("delete success")
except Exception as e:
    print("file doesn't exist")