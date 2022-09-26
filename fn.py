import os
import pynput
import playsound
from pynput import keyboard
from playsound import playsound

def on_press(key):
    key_str = '{0}'.format(key)
    if (key_str == '<179>'):
        stream = os.popen('/usr/local/bin/issw')
        output = stream.read().strip()
        if (output == 'com.apple.keylayout.ABC'):
            os.system('/usr/local/bin/issw com.apple.keylayout.Russian')
            playsound('/Users/#USER#/knopka-klik-zvonkii-myagkaya.wav')
        else:
            os.system('/usr/local/bin/issw com.apple.keylayout.ABC')
            playsound('/Users/#USER#/knopka-klik-zvonkii-myagkaya.wav')


with keyboard.Listener(on_press=on_press, on_release=None) as listener:
    listener.join()
