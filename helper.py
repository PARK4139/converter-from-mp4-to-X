from moviepy.editor import *
import os

os.system("chcp 65001")

file_origin = sys.argv[1]
print(f'from : {file_origin}')
file_edited = f'{os.path.splitext(os.path.basename(file_origin))[0]}.wav'
print(f'to   : {file_edited}')
if os.path.splitext(os.path.basename(file_origin))[1]== '.mp4':
    
    videoclip = VideoFileClip(file_origin)
    audioclip = videoclip.audio
    os.system('mkdir storage')
    os.chdir('storage')

    # audioclip.write_audiofile(file_edited)
    # audioclip.write_audiofile(file_edited, fps= 8000 )
    audioclip.write_audiofile(file_edited, fps= 44100  )
    audioclip.close()
    videoclip.close()
 