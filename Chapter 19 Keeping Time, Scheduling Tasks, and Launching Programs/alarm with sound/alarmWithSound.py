#Chapter 19 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter19.html

import datetime, os, subprocess, time

def alarm_with_audio(alarm_time, audio_filename):
    if not os.path.exists(audio_filename):
        raise Exception('Cannot find file ' + str(audio_filename))

    while datetime.datetime.now() < alarm_time:
        time.sleep(0.1)
    
    subprocess.run(['start', audio_filename], shell=True)


now = datetime.datetime.now()
alarm_timer = datetime.timedelta(seconds=3)
alarm_with_audio(now + alarm_timer, 'alarm.wav')