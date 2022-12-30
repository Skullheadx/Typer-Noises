import threading
import time
import os
from pygame import mixer
from pynput import keyboard

TEXT_PATH = "copy-pastas/"

delay = 0.025  # delay between each character typed in seconds.

keys = {eval(f"keyboard.Key.f{i + 1}"): "" for i in range(12)}
scripts = []
for root, dirs, files in os.walk(TEXT_PATH):
    for i, x in enumerate(zip(files, keys)):
        file, key = x
        with open(os.path.join(TEXT_PATH, file), "r") as f:
            keys[key] = f.read().replace("â€™", "'")

# Sound
mixer.init()
mixer.music.load("reddit-admin-typing.mp3")
mixer.music.set_volume(0.5)

# to stop typing before end.
stopped = False


def typer(text):
    global stopped
    mixer.music.play(-1)
    k = keyboard.Controller()
    for char in text:
        if char == "\n":
            char = keyboard.Key.enter
        k.press(char)
        time.sleep(delay)
        k.release(char)
        if stopped:
            break
    mixer.music.stop()


def on_press(key):
    global stopped
    if key in keys:  # having another thread so we can detect input while typing
        stopped = False
        t = threading.Thread(target=typer, args=[keys[key]])
        t.start()
    elif key == keyboard.Key.pause:
        stopped = True
    elif key == keyboard.Key.esc:
        quit()


with keyboard.Listener(on_press=on_press) as listener:  # listening for events
    listener.join()
