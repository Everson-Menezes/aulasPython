from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download(url, option):
    yt = YouTube(url)
    path = path_select()
    # Print video details
    print("Title:", yt.title)
    print("Views:", yt.views)
    print("Length:", yt.length, "seconds")
    if option == "video":
        # Select the highest resolution stream
        resolution.set = yt.streams.get_highest_resolution()

        stream = yt.streams.get_by_resolution(resolution)
        # Download the video
        stream.download(output_path=path)
        return "Video downloaded successfully!"
    if option == "audio":
        # Optional: Download only the audio
        audio_stream = yt.streams.get_audio_only()
        audio_stream.download(output_path=path)
        return "Audio downloaded successfully!"


def path_select():
    # Create the root Tkinter window
    root = tk.Tk()
    root.withdraw()
    # Open the file selection dialog
    return filedialog.askdirectory()


def button_clicked():
    option = var.get()
    url = inputUrl.get()
    result.set = download(url, option)


# Cria a janela principal
window = tk.Tk()

# Configurações da janela
window.title("YouTube-Videos")
window.geometry("400x300")
var = tk.StringVar()
result = tk.StringVar()
resolution = tk.StringVar()
lblUrl = tk.Label(window, text="Input URL")
lblUrl.pack()
inputUrl = tk.Entry(window)
inputUrl.pack()
rbAudio = tk.Radiobutton(window, text="Audio", variable=var, value="audio")
rbAudio.pack()
rbVideo = tk.Radiobutton(window, text="Video", variable=var, value="video")
rbVideo.pack()
btnDownload = tk.Button(window, text="Download", command=button_clicked)
btnDownload.pack()
lblResult = tk.Label(window, text=result)
lblUrl.pack()

# Inicia o loop principal da aplicação
window.mainloop()