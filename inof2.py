import speech_recognition as sr
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from gtts import gTTS
from pprint import pprint
from playsound import playsound
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import re


def train(trainer):
    conversation = [
        "",
        "Maaf, silahkan ulangi",
        "Halo",
        "Halo, nama saya Ino. Saya adalah asisten virtual B4T. Ada yang bisa saya bantu?",
        "ada agenda apa hari ini",
        "Diseminasi Hasil Litbangyasa 2019",
        "oke mas Ino, open please",
        "Password please",
        "B4T",
        "Maaf salah",
        "budi susanto",
        "Password diterima. Membuka acara seminar."
    ]
    trainer.train(conversation)
def recognize(r,audio):
    try:
        return r.recognize_google(audio, language = 'id-ID')
    except:
        return ''

def stem(factory,sentence):
    return output

def speak(chatbot,output,i):
    response = chatbot.get_response(output)
    mytext = str(response)
    pprint(mytext)
    if mytext == '':
        mytext = "Maaf, silahkan ulangi"
        
    myobj = gTTS(text=mytext, lang='id')
    myobj.save("speech"+str(i)+".mp3")
    playsound("speech"+str(i)+".mp3")    
    if mytext == "Password diterima. Membuka acara seminar.":
        playsound("siren.mp3")

def play():
    chatbot = ChatBot('ino2')
    trainer = ListTrainer(chatbot)
    r = sr.Recognizer()
    i = 0
    with sr.Microphone() as source:
        while True:
            i+=1
            print("SILAHKAN BICARA:")
            playsound("beep.mp3")
            audio = r.listen(source)
            words = recognize(r,audio)
            print("WAKTU BICARA SELESAI, TERIMA KASIH.")
            factory = StemmerFactory()
            stemmer = factory.create_stemmer()
            output = stemmer.stem(words)
            pprint(output)
            if output == "Password diterima. Membuka acara seminar.":
                playsound("siren.mp3")
                break
            elif output =="train":
                train(trainer)
            else:
                speak(chatbot,output,i)
                
play()