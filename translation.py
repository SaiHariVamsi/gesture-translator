import os
import sys
import time
import pygame
from gtts import gTTS
from googletrans import Translator

translator = Translator()

def translate(text_to_translate, opt):
    if opt == 1:
        translation = translator.translate(text_to_translate, dest="hi")
    elif opt == 2:
        translation = translator.translate(text_to_translate, dest="bn")
    elif opt == 3:
        translation = translator.translate(text_to_translate, dest="mr")
    elif opt == 4:
        translation = translator.translate(text_to_translate, dest="te")
    elif opt == 5:
        translation = translator.translate(text_to_translate, dest="ta")
    elif opt == 6:
        translation = translator.translate(text_to_translate, dest="gu")
    elif opt == 7:
        translation = translator.translate(text_to_translate, dest="ur")
    elif opt == 8:
        translation = translator.translate(text_to_translate, dest="kn")
    elif opt == 9:
        translation = translator.translate(text_to_translate, dest="or")
    else:
        translation = translator.translate(text_to_translate, dest="ml")
    return translation.text

def voice(text, opt):
    translated_text = text
    lang_code = opt

    langs = {1:'hi', 2:'bn', 3:'mr', 4:'te', 5:'ta', 6:'gu', 7:'ur', 8:'kn', 9:'or', 10:'ml'}

    tts = gTTS(text=translated_text, lang=langs[lang_code])
    tts_file = 'output.mp3'
    tts.save(tts_file)
    pygame.mixer.init()
    pygame.mixer.music.load(tts_file)
    pygame.mixer.music.play()

    print("Playing...")  
    time.sleep(2)

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()

    print("Done!")