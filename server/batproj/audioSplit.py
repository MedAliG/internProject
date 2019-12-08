from os import path
from pydub import AudioSegment
import time


def splitFn(audioPath,sourceAudio):
    res = []
    audioFile = AudioSegment.from_file(audioPath)
    fragNumber = len(audioFile)//8
    start = 0
    end = 8
    for x in range fragNumber:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        soundSegment = sound[start:end]
        start +=8
        if start > len(audioFile-8):
            end = audioFile-start
        else 
            end +=8
        soundSegment.export("/data/frags/".str(x).current_time.".mp3",format="mp3")
        