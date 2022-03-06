from __future__ import unicode_literals 
from yt_dlp import YoutubeDL as ytdl
import log
import urllib.request as urR
import urllib.error as urE
import dir


options = ['Y','y', 'N', 'n']
check = None


def url_input():
    check = False
    url = None

    while True:
        # awful solution, I know.
        url = input('Enter Youtube URL: ')
        if(len(url) > 42):
            break
        print("Invalid URL. Try Again.\n")

    req = urR.Request(url)
    try:
        response = urR.urlopen(req)
    except urE.HTTPError as error:
        print("Failed to Reach Server\nError Code:", error.code)
        check = True    
    except urE.URLError as error:
        print("Could not fulfill the Request\nError Code:",error.reason)
        check = True
    

    return check,url   


def video_progress(status):
    if status['status'] == 'finished':
        print('\nDownload Finsihed') 

def audio_progress(status):
    if status['status'] == 'finished':
        print('\nDownload Finsihed, Converting to MP3...') 



def yt_dl():

    request_check = True
    output_options = None
    avoptions = None

    while request_check:
        request_check,url = url_input()

    while True:

        avoptions = input("Download Video or Convert to Audio? [1 for Video, 2 for Audio]: ")
        if(avoptions == '1'):
            
            output_options = {
               
                'logger': log.Log(),
                'progress_hooks': [video_progress],
                'outtmpl': dir.VIDEO_PATH + '/%(title)s.%(ext)s',  
            }
            break

        if(avoptions == '2'):

            output_options = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }], 
                'logger': log.Log(),
                'progress_hooks': [audio_progress],
                'outtmpl': dir.AUDIO_PATH + '/%(title)s.%(ext)s',
            }
            break
        else:
            print("Input invalid. Please press either 1 or 2.\n")            


    with ytdl(output_options) as ydl:
        ydl.download([url])


while True:

    
    dir.dw_dirs()
    yt_dl()

    while True:
        check = input("Convert another URL? [Y/N]: ")
        if check not in options:
            print("Error: Press a valid key.")
        else:
            break    

    if check in options[2:]:
        break                                        
    dir.clear_screen()