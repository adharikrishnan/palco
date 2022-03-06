import os

VIDEO_PATH = "Downloads/Video"
AUDIO_PATH = "Downloads/Audio"

def make_dir(dir_name, dir_parent, msg=None):

    dir_path = os.path.join(str(dir_parent), str(dir_name))
    exists = os.path.exists(dir_path)
    
    if not exists:
        os.mkdir(dir_path)
        if (msg is not None):
            print(msg)

def dw_dirs():
    make_dir("Downloads","")
    make_dir("Video", "Downloads/",)
    make_dir("Audio", "Downloads/",)

def clear_screen():

    if os.name == 'nt':
        _ = os.system('cls')       
    



  




