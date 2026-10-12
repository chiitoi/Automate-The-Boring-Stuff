#Chapter 24 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter24.html

import whisper, srt, os

def find_in_audio(audio_filename, search_word):
    # Convert search_word to lowercase for case-insensitive matching:xxxxx
    search_word = search_word.lower()
    
    # Check if the subtitle file already exists:
    if not os.path.exists(audio_filename[:-4] + '.srt'):
        # Transcribe the audio file:
        model = whisper.load_model('base')
        result = model.transcribe(audio_filename)

        # Create the subtitle file:
        write_function = whisper.utils.get_writer('srt', '.')
        write_function(result, audio_filename)

    # Read in the text contents of the subtitle file:
    with open(audio_filename[:-4] + '.srt', encoding='utf-8') as file_obj:
        content = file_obj.read()

    # Go through each subtitle and collect timestamps of matches:
    found_timestamps = []
    for subtitle in srt.parse(content):
        if search_word in subtitle.content.lower():
            found_timestamps.append(str(subtitle.start))

    # Return the list of timestamps:
    return found_timestamps

print(find_in_audio('DNA_lecture.mp3', 'amino'))