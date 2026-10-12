#Chapter 24 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter24.html

import whisper, yt_dlp
from pathlib import Path
video_url = ''

#grab the video id at the end of the url
video_id = video_url.split('v=')[1]
with yt_dlp.YoutubeDL() as ydl:
    ydl.download([video_url])

#search for the file name
matching_filenames = list(Path().glob(f'*{video_id}*'))
downloaded_filename = str(matching_filenames[0])

print(f"\nVideo: {downloaded_filename}\n")

#create subtitle file
model = whisper.load_model('base')
result = model.transcribe(downloaded_filename)
write_function = whisper.utils.get_writer('srt', '.')
write_function(result, downloaded_filename)

print('\nSubtitle created!')
