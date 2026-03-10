import os
import pandas as pd 
from gtts import gTTS
from pydub import AudioSegment

def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=True)
    myobj.save(filename)

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')  
    start = 0
    finish = 5000
    audio[start:finish].export("1_hindi.mp3", format="mp3")

    audio = AudioSegment.from_mp3('railway.mp3')  
    start = 11500
    finish = 13000
    audio[start:finish].export("3_hindi.mp3", format="mp3")

    audio = AudioSegment.from_mp3('railway.mp3')  
    start = 49000
    finish = 50000
    audio[start:finish].export("5_hindi.mp3", format="mp3")

    audio = AudioSegment.from_mp3('railway.mp3')  
    start = 51000
    finish = 52000
    audio[start:finish].export("7.1_hindi.mp3", format="mp3")

    audio = AudioSegment.from_mp3('railway.mp3')  
    start = 35000
    finish = 36500
    audio[start:finish].export("7_hindi.mp3", format="mp3")

    audio = AudioSegment.from_mp3('railway.mp3')  
    start = 52000
    finish = 56000
    audio[start:finish].export("9_hindi.mp3", format="mp3")

    audio = AudioSegment.from_mp3('railway.mp3')  
    start = 56000
    finish = 57500
    audio[start:finish].export("11_hindi.mp3", format="mp3")

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)

    for index, item in df.iterrows():
        textToSpeech(item['fron'], "2_hindi.mp3")
        textToSpeech(item['via'], "4_hindi.mp3")
        textToSpeech(item['to'], "6_hindi.mp3")
        textToSpeech(str(item['train_no']) + " " + item['train_name'], "8_hindi.mp3")
        textToSpeech(item['platform'], "10_hindi.mp3")

        audios = [
            "1_hindi.mp3",
            "2_hindi.mp3",
            "3_hindi.mp3",
            "4_hindi.mp3",
            "5_hindi.mp3",
            "6_hindi.mp3",
            "7_hindi.mp3",
            "7.1_hindi.mp3",
            "8_hindi.mp3",
            "9_hindi.mp3",
            "10_hindi.mp3",
            "11_hindi.mp3"
        ]

        announcement = mergeAudios(audios)
        announcement.export(
            f"announcement_{item['train_no']}_{index+1}.mp3",
            format="mp3"
        )

if __name__ == "__main__":              
    print("Generating skeleton....")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announcement_hindi.xlsx")
