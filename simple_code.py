import threading  # to detect inputs and type at the same time
import time  # to add delay between key presses
from pygame import mixer  # For the typing noises
from pynput import keyboard  # For monitoring and controlling the keyboard

with open(f"text.txt", "r") as f:  # opens and reads the text file text.txt
    text = f.read()  # f is the file and we can get the text contents using f.read()
    # using with open so that the file is closed when we are done

delay = 0.025  # delay between each character typed in seconds.

# Sound
mixer.init()  # Initialise mixer so that we can play sounds using pygame
mixer.music.load("reddit-admin-typing.mp3")  # Typing sound effect we will be using


def typer():  # function that will run when we want to type something
    mixer.music.play(-1)  # begin playing the typing sound. -1 so that it loops infinitely
    k = keyboard.Controller()  # so that we can create key presses
    for char in text:  # loop through each character in the text
        if char == "\n":  # if it is a new line character, this is a special case for pynput
            char = keyboard.Key.enter  # simply change the value of char so that the correct character is typed
        k.press(char)  # to press down a key (KEY DOWN)
        time.sleep(delay)  # pause this thread for delay time
        k.release(char)  # let go of a key (KEY UP)
    mixer.music.stop()  # stop the typing noises once we have finished typing everything


def on_press(key):  # this function is called every time a key is pressed
    if key == keyboard.Key.f2:  # if the f2 key is pressed (function keys at the top of the keyboard)
        t = threading.Thread(target=typer)  # having another thread so we can detect input while typing
        t.start()  # begin typing
    elif key == keyboard.Key.esc:  # Close the program when escape key is pressed
        listener.stop()  # stops listening for key presses which then terminates the program


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()  # starting listening thread
    # it will continuously listen for key presses and will run the on_press function when a key is pressed
