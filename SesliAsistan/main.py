# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 18:11:02 2021

@author: emirh
"""
import sys
import speech_recognition as sr
import webbrowser 
import pyglet
import time
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem             
from PyQt5 import QtCore # timer için

from sesliasistan import *


app1=QtWidgets.QApplication(sys.argv)
MainWindow1=QtWidgets.QMainWindow()
ui1= Ui_MainWindow() #Bu satır değişir
ui1.setupUi(MainWindow1)
MainWindow1.show()

r =  sr.Recognizer()
mic = sr.Microphone()

def sesliKomut(): #ses algılama fonksiyonu
    
    with mic as m:
        print("ses algılaniyor...")
        ui1.statusbar.showMessage(" "*1 + " Ses algılanıyor...", 1500)
        audio = r.record(m, duration=4)
        text  = r.recognize_google(audio,language='tr-TR')
        print("ses algilama bitti")
        return text
  
def calistir():
    textListen = sesliKomut()
    text=textListen.lower()
    print(text)
    ui1.label.setText(str(text))
    if(text=="kapat" or text==""):
        print("sistem kapatılıyor.")
        MainWindow1.Close()
    elif(text.find('merhaba')!=-1 or text.find('selam')!=-1 or text.find('selamun aleyküm')!=-1) : 
        music=pyglet.resource.media("merhaba.mp3")
        music.play()
    elif(text.find('ne haber')!=-1 or text.find('nasılsın')!=-1 or text.find('nasıl gidiyor')!=-1):
        music=pyglet.resource.media("iyiyim.mp3")
        music.play()
    elif(text.find('masal anlatır mısın')!=-1 or text.find('hikaye anlatır mısın')!=-1):
        music=pyglet.resource.media("hikaye.mp3")
        music.play()
    elif(text.find('google aç')!=-1) : 
        webbrowser.open("https://google.com")
    elif("en iyi teknoloji sayfası" in text):
        music=pyglet.resource.media("teknobol.mp3")
        music.play()
    elif(text.find('acıktın mı')!=-1 or text.find('ne yemek istersin')!=-1 or text.find('karnın aç mı')!=-1):
        music=pyglet.resource.media("pil.mp3")
        music.play()
    elif(text.find('tanıştığıma memnun oldum')!=-1 or text.find('tanışalım mı')!=-1 or text.find('sen kimsin')!=-1):
        music=pyglet.resource.media("tanisma.mp3")
        music.play()
    elif(text.find('müzik söyler misin')!=-1 or text.find('şarkı söyler misin')!=-1 or text.find('sesin güzel mi')!=-1):
        music=pyglet.resource.media("muzik.mp3")
        music.play()
    else:
        music=pyglet.resource.media("uzgunum.mp3")
        music.play()
    
ui1.pushButton.clicked.connect(calistir)

sys.exit(app1.exec_())