import threading
import time
import pyautogui
from pygame import mixer
from pynput import keyboard


with open("test.txt", "r") as f:
    script = f.read()

mixer.init()

mixer.music.load("reddit-admin-typing-14393.mp3")
mixer.music.set_volume(0.5)

delay = 0.01

def typer():
    mixer.music.play(-1)
    k = keyboard.Controller()
    for char in script:
        if char == keyboard.Key.enter:
            char = keyboard.Key.enter
        k.press(char)
        time.sleep(delay)
        k.release(char)
    mixer.music.stop()


def on_press(key):
    if key == keyboard.Key.f5:
        t = threading.Thread(target=typer)
        t.start()
    if key == keyboard.Key.esc:
        quit()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()