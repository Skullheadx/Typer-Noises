import time  # to add delay between key presses
from pygame import mixer  # For the typing noises
from pynput import keyboard  # For controlling the keyboard

with open(f"text.txt", "r") as f:  # opens and reads the text file text.txt
    text = f.read()  # f is the file and we can get the text contents using f.read()
    # using with open so that the file is closed when we are done

delay = 0.05  # delay between each character typed in seconds. less delay means faster typing

# Sound
mixer.init()  # Initialise mixer so that we can play sounds using pygame
mixer.music.load("reddit-admin-typing.mp3")  # Typing sound effect we will be using


def type_text():
    mixer.music.play(-1)  # begin playing the typing sound. -1 so that it loops infinitely or if we stop it
    k = keyboard.Controller()  # so that we can create key presses
    for char in text:  # loop through each character in the text
        if char == "\n":  # if it is a new line character, this is a special case for pynput
            char = keyboard.Key.enter  # simply change the value of char so that the correct character is typed
        k.press(char)  # to press down a key (KEY DOWN)
        time.sleep(delay)  # pause the code for delay time
        k.release(char)  # let go of a key (KEY UP)
    mixer.music.stop()  # stop the typing noises once we have finished typing everything


time.sleep(3)  # this will give you 3 seconds to change windows and find where you want to type
type_text()  # run the function and type out the text
