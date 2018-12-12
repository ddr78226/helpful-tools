"""A demo of the Google CloudSpeech recognizer."""
import threading
import time
import os
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import pygame
import sys


class musicThread(threading.Thread):
    def __init__(self, threadID, name, mode):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.mode = mode
    def run(self):
      pygame.init()
      pygame.mixer.init()
      pygame.time.delay(1000)
      pygame.mixer.music.load('Girls_Like_You.mp3')
      pygame.mixer.init(frequency=15500,size=-16,channels=4)
      pygame.mixer.music.set_volume(0.1)
      pygame.mixer.music.play()
      while True:
       for event in pygame.event.get():
        if event.type == pygame.QUIT:
         sys.exit
      pygame.mixer.music.close()
class musicThread2(threading.Thread):
    def __init__(self, threadID, name, mode):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.mode = mode
    def run(self):
      pygame.init()
      pygame.mixer.init()
      pygame.time.delay(1000)
      pygame.mixer.music.load('Sugar.mp3')
      pygame.mixer.init(frequency=15500,size=-16,channels=4)
      pygame.mixer.music.set_volume(0.1)
      pygame.mixer.music.play()
      while True:
       for event in pygame.event.get():
        if event.type == pygame.QUIT:
         sys.exit
      pygame.mixer.music.close()

def main():
      recognizer = aiy.cloudspeech.get_recognizer()
      recognizer.expect_phrase('turn off the light')
      recognizer.expect_phrase('turn on the light')
      recognizer.expect_phrase('blink')
      recognizer.expect_phrase('repeat after me')
      recognizer.expect_phrase('where am I')
      recognizer.expect_phrase('play music')
      recognizer.expect_phrase('play next song')

      thread1 = musicThread(1,"musicThread",1)
      thread2 = musicThread2(2,"musicThread",1)
      button = aiy.voicehat.get_button()
      led = aiy.voicehat.get_led()
      aiy.audio.get_recorder().start()

      while True:
        print('Press the button and speak')
        button.wait_for_press()
        print('Listening...')
        text = recognizer.recognize()
        if text is None:
            print('Sorry, I did not hear you.')
        else:
            print('You said "', text, '"')
            if 'turn on the light' in text:
                led.set_state(aiy.voicehat.LED.ON)
            elif 'turn off the light' in text:
                led.set_state(aiy.voicehat.LED.OFF)
            elif 'blink' in text:
                led.set_state(aiy.voicehat.LED.BLINK)
            elif 'repeat after me' in text:
                to_repeat = text.replace('repeat after me', '', 1)
                aiy.audio.say(to_repeat)
            elif 'where am I' in text:
                aiy.audio.say('Providence University')
            elif 'play music' in text:
              #aiy.audio.play_audio(os.path.abspath("Girls_Like_You.mp3"))
               thread1.start()
               # print('123')
            elif 'play next song' in text:
               aiy.audio.say('play Maroon 5 Sugar')
               thread2.start()
            elif 'goodbye' in text:
                os._exit(0)

if __name__ == '__main__':
    main()

