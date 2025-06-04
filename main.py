import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
import moviepy

# sample video: https://youtu.be/j7W2v_FmCuE?si=7ebbHZ8Q5L6UqZJG
def download():
    url = 'https://youtu.be/j7W2v_FmCuE?si=7ebbHZ8Q5L6UqZJG'
    try:
        YouTube(url).check_availability()
    except Exception as e:
        messagebox.showinfo("Error" ,"video is not available. check link again.")
        return
    print("Video URL:", url)
    mp4 = YouTube(url).streams.get_highest_resolution().download()
    videoclip = moviepy.VideoFileClip(mp4)
    videoclip.close()
    # mp4.write_videofile("video.mp4")
    
    

def select_folder():
    directory = filedialog.askdirectory()
    print("Video to be downloaded at:", directory)
    destination_label.config(text=directory)

root = tk.Tk()
root.title("YT Video Downloader")
root.resizable(0, 0)
canvas = tk.Canvas(root, height=300, width=400)
canvas.pack()

app_label = tk.Label(root, text="Youtube Video Downloader", fg="white", font=("Arial", 15))
canvas.create_window(200, 50, window=app_label)

link_label = tk.Label(root, text="Enter Video's Link", fg="white", font=("Arial", 10))
link_entry = tk.Entry(root)
canvas.create_window(200, 100, window=link_label)
canvas.create_window(200, 120, window=link_entry)

destination_label = tk.Label(root, text=r"{Select Destination Folder}", fg="white", font=("Arial", 10))
select_folder_button = tk.Button(root, text="Select", command=select_folder)
canvas.create_window(200, 160, window=destination_label)
canvas.create_window(200, 190, window=select_folder_button)

download_button = tk.Button(root, text="Download Video", command=download, height=2)
canvas.create_window(200, 250, window=download_button)
root.mainloop()