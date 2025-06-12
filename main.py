import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from yt_dlp import YoutubeDL

# sample video: https://youtu.be/j7W2v_FmCuE?si=7ebbHZ8Q5L6UqZJG
def download():
    print("hellp")
    url = link_entry.get()
    print("hellp")
    download_path = destination_label.cget("text")
    print("hellp")
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'quiet': False,
        'merge_output_format': 'mp4',
        'outtmpl': f'{download_path}/%(title)s.%(ext)s'
    }
    print("hellp")
    print(download_path)
    
    #not working
    if str(download_path) == "{Select Destination Folder}" and not download_path:
        return
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        messagebox.showerror("Video downloading failed", str(e))
    else:
        messagebox.showinfo("Video download completed")
        
    
    
def select_folder():
    directory = filedialog.askdirectory()
    print("Video to be downloaded at:", directory)
    destination_label.config(text=directory)




if __name__ == '__main__':
    #GUI
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