from moviepy.editor import *
import os

os.system("chcp 65001")

file_origin = sys.argv[1]
print(f'file_origin : {file_origin}')
file_edited = f'{os.path.splitext(os.path.basename(file_origin))[0]}.{sys.argv[2]}'
print(f'{file_edited} 로 변환 시도하고 있습니다.')
if os.path.splitext(os.path.basename(file_origin))[1]== '.mp4':
    if sys.argv[2] == 'mp3':
        mp3_file = f'{os.path.splitext(os.path.basename(file_origin))[0]}.{sys.argv[2]}'
        
        videoclip = VideoFileClip(file_origin)
        audioclip = videoclip.audio
        # audioclip.write_audiofile(mp3_file)
        # audioclip.write_audiofile(mp3_file, fps= 8000 )
        os.system('mkdir downloads')
        os.chdir('downloads')

        audioclip.write_audiofile(mp3_file, fps= 44100  )
        audioclip.close()
        videoclip.close()

    if sys.argv[2] == 'wav':
            wav_file = f'{os.path.splitext(os.path.basename(file_origin))[0]}.{sys.argv[2]}'
            
            videoclip = VideoFileClip(file_origin)
            audioclip = videoclip.audio
            # audioclip.write_audiofile(wav_file)
            # audioclip.write_audiofile(wav_file, fps= 8000 )
            os.system('mkdir downloads')
            os.chdir('downloads')

            audioclip.write_audiofile(wav_file, fps= 44100  )
            audioclip.close()
            videoclip.close()

    if sys.argv[2] == 'flac':
            flac_file = f'{os.path.splitext(os.path.basename(file_origin))[0]}.{sys.argv[2]}'
            
            videoclip = VideoFileClip(file_origin)
            audioclip = videoclip.audio
            # audioclip.write_audiofile(flac_file)
            # audioclip.write_audiofile(flac_file, fps= 8000 )
            os.system('mkdir downloads')
            os.chdir('downloads')

            audioclip.write_audiofile(flac_file, fps= 44100  )
            audioclip.close()
            videoclip.close()


