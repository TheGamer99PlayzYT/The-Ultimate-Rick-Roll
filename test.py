# MIT License

# Copyright (c) 2023 TheGamer99PlayzYT

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import tkinter as tk
import pyautogui
from moviepy.editor import VideoFileClip
import subprocess
import sys
import os

def show_dialog():
    dialog = tk.Toplevel(root)
    dialog.title("You Really don't listen.")

    def handle_close():
        root.quit()
        
    dialog.protocol("WM_DELETE_WINDOW", handle_close)
    
    label = tk.Label(dialog, text="I told you don't click on this.. Don't press continue")
    label.pack(padx=20, pady=10)
    
    continue_button = tk.Button(dialog, text="Continue", command=lambda: show_next_dialog(dialog))
    continue_button.pack(side=tk.LEFT, padx=10, pady=10)

def show_next_dialog(dialog):
    dialog.withdraw()

    next_dialog = tk.Toplevel(root)
    next_dialog.title("You're very predictable.")

    def handle_close():
        root.quit()
        
    next_dialog.protocol("WM_DELETE_WINDOW", handle_close)
    
    label = tk.Label(next_dialog, text="I can guess your next move. Let's have some fun with this one. Don't press okay.")
    label.pack(padx=20, pady=10)
    
    okay_button = tk.Button(next_dialog, text="Okay", command=lambda: show_next_dialog2(next_dialog))
    okay_button.pack(side=tk.LEFT, padx=10, pady=10)

def show_next_dialog2(dialog):
    dialog.withdraw()

    next_dialog = tk.Toplevel(root)
    next_dialog.title("Oops")

    def handle_close():
        root.quit()
        
    next_dialog.protocol("WM_DELETE_WINDOW", handle_close)
    
    label = tk.Label(next_dialog, text="You've just launched a nuke and it's coming for your PC heheheh. The only way to stop it is to press stop!")
    label.pack(padx=20, pady=10)
    
    stop_button = tk.Button(next_dialog, text="Stop", command=lambda: start_countdown(next_dialog))
    stop_button.pack(side=tk.LEFT, padx=10, pady=10)

def start_countdown(dialog):
    dialog.withdraw()

    countdown_dialog = tk.Toplevel(root)
    countdown_dialog.title("Countdown")

    def handle_close():
        root.quit()
        
    countdown_dialog.protocol("WM_DELETE_WINDOW", handle_close)

    countdown_label = tk.Label(countdown_dialog, text="")
    countdown_label.pack(padx=20, pady=10)
    
    seconds = 10 
    
    def update_countdown():
        nonlocal seconds
        
        countdown_label.config(text=f"Time remaining: {seconds} seconds")
        seconds -= 1
        
        if seconds >= 0:
            countdown_label.after(1000, update_countdown)
        else:
            countdown_label.destroy()
            countdown_dialog.withdraw()
            start_video()

    update_countdown()

def start_video():
    pyautogui.press('volumeup')
    
    video_file = os.path.join(os.path.dirname(__file__), "rickroll.mp4")
    
    video_clip = VideoFileClip(video_file)
    
    video_clip.preview()
    video_clip.close()
    
    shutdown()

def shutdown():
    countdown_dialog = tk.Toplevel(root)
    countdown_dialog.title("Shutdown")

    def handle_close():
        root.quit()
        
    countdown_dialog.protocol("WM_DELETE_WINDOW", handle_close)

    countdown_label = tk.Label(countdown_dialog, text="")
    countdown_label.pack(padx=20, pady=10)
    
    seconds = 10
    
    def update_countdown():
        nonlocal seconds
        
        countdown_label.config(text=f"Your PC will self-destruct in T-{seconds}")
        seconds -= 1
        
        if seconds >= 0:
            countdown_label.after(1000, update_countdown)
        else:
            countdown_label.destroy()
            shutdown_command = "shutdown /s /t 0"
            subprocess.run(shutdown_command, shell=True)
    
    update_countdown()

root = tk.Tk()
root.withdraw()
show_dialog()
root.mainloop()
