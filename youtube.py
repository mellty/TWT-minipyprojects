# Followed along from "3 Python Automation Projects - For Beginners", https://www.youtube.com/watch?v=zT7niRUOs9o

from pytube import YouTube
import tkinter as tk # simple 2d GUI library, comes with Python
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully")

    except Exception as e:
        print(e)

# url = "https://www.youtube.com/watch?v=zT7niRUOs9o"
# save_path = "/Users/MellatMafei/Desktop"

# download_video(url, save_path)
        
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder: 
        print(f"Selected folder: {folder}")

    return folder
    

# checks if the youtube.py script is being imported into another script as a module or if it's a standalone program
# this matters because it lets you control what is run in this script depending on how/if it's being used
# so it's a convention. atm nothing is using youtube.py so it doesn't matter
if __name__ == "__main__": 
    root = tk.Tk() # instantiates Tk module, creates a Tk window. needed to use the file dialog
    root.withdraw() # hides the Tk window because it's unneeded for the file dialog. only care about root

    video_url = input("Pls enter a YouTube url: ")
    save_dir = open_file_dialog()

    if not save_dir:
        print("Invalid save location")
    else:
        download_video(video_url, save_dir)