'''
    itWorks - A little script that notifies you when your
              internet is up.
'''

import subprocess
import time
import pygame.mixer
import os

pygame.mixer.init()

cmd = "ping www.google.com -c 4"
title = "Notification"
message = "Your Internet is now working."
sound_file = 'data/sound.ogg'
icon = os.path.join(os.getcwd(),'data/icon.png')

def play_notification_sound(file_path):
    sound = pygame.mixer.Sound(file_path)
    channel = sound.play()
    while channel.get_busy():
        time.sleep(1)


def ping():
    p = subprocess.call(cmd,
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    # I've passed stdout=subprocess.PIPE to call() to supress any output.
    return p

def main():
    try:
        while True:
            result = ping()
            if result == 0:
                subprocess.call("notify-send '{}' '{}' -i {}".format(title, message, icon),
                                                                    shell=True)
                play_notification_sound(sound_file)
                break
            else:
                time.sleep(4)
    except KeyboardInterrupt:
        print "\b\bExiting"

if __name__ == '__main__':
    main()
