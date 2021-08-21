import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def texttoSpeech(text,filename):
    mytext= str(text)
    language= 'hi'
    myobj = gTTS(text= mytext,lang=language,slow=False)
    myobj.save(filename)

def mergeaudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined +=AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    #1- Making- Kripya dhyan dijiye 
    audio=AudioSegment.from_mp3('railway.mp3')
    start=88000
    finish=90200
    audioProcessed=audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format ="mp3")

    #2- form city

    #3- Genrate se chalkar
    start=91000
    finish=92200
    audioProcessed=audio[start:finish]
    audioProcessed.export("3_hindi.mp3",format ="mp3")

    #4- via city

    #5-Genrate se raste
    start=94000
    finish=95000
    audioProcessed=audio[start:finish]
    audioProcessed.export("5_hindi.mp3",format ="mp3")

    #6- to city

    #7-generate ko jane wali gadi sankhya 
    start=96000
    finish=98900
    audioProcessed=audio[start:finish]
    audioProcessed.export("7_hindi.mp3",format ="mp3")

    #8- train no. and name

    #9- Generate kuch hi samay mein platform no.
    start=105500
    finish=108200
    audioProcessed=audio[start:finish]
    audioProcessed.export("9_hindi.mp3",format ="mp3")

    #10-  platform no.

    #generate pr aa rhi hai
    start=109000
    finish=112250
    audioProcessed=audio[start:finish]
    audioProcessed.export("11_hindi.mp3",format ="mp3")

def generateAnnouncement(filename):
    df= pd.read_excel(filename)
    print(df)

    for index,item in df.iterrows():
       #2-Generate form city
       texttoSpeech(item['from'], '2_hindi.mp3')
       #4-Generate via city
       texttoSpeech(item['via'], '4_hindi.mp3')
       #6-Generate to city
       texttoSpeech(item['to'], '6_hindi.mp3')
       #8-Generate train no. and name
       texttoSpeech(item['train_no'] +" "+item['train_name'] , '8_hindi.mp3')
       #10-Generate platform no.
       texttoSpeech(item['platform'], '10_hindi.mp3')

       audios =[f"{i}_hindi.mp3" for i in range(1,12)]

       announcement =mergeaudios(audios)
       announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format="mp3")


if __name__=="__main__":
    print("Generate Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")


    

