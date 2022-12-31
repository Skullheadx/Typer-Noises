# Typer-Noises

Source code for a program that types out text for you. Use this to prank you friends! Enjoy!

_If you are a beginner coder, I recommend looking through the simple-code branch as it is much less complicated than this code._
-------------------------------------------------------------------------------------------------------------
HOW TO USE:
1. Download the code
2. Extract all from the .zip file in your downloads folder
3. Run the Copypasta Typer.exe file
4. Press the function keys located at the top of the keyboard (i.e. F1, F2, F3, and so on) to type out the text
5. Press the PAUSE key to stop typing text at any time
6. Press the ESCAPE key to completely stop the program

HOW TO ADD YOUR OWN COPYPASTAS:
1. Go inside the copypastas folder located inside the extracted zip folder
2. Delete all the .txt files
3. Create your own .txt file with whatever text you want*
4. You can create up to 12 different text files each with their own function key from F1 to F12 (Note that the function key that coresponds to each text file is in alphabetical order.)

*_Some special characters do not work with pynput library I used to code this program, so you may have to remove them or replace them with other characters_

HOW TO CHANGE THE TYPING SPEED:
1. Open the main.py file using Python
2. Make sure all dependencies have been installed using `pip install pygame` and `pip install pynput` in the terminal
3. Change the delay variable to the desired amound of time in seconds per character (Smaller delay will result in faster typing speed)

-------------------------------------------------------------------------------------------------------------
EXTRAS:
Check out the other branches for extensions on this project.

WPM-shower - will output the Words Per Minute at the end of each operation
bee-movie-typer-game - type out the entire bee movie game
simple-code - simpler code for beginners
