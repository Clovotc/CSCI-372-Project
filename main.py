# This is the combined code of both GUI and YouTUbe files
# Maison Kasprick - 11/7/2024
# Version 1.1

# Imports
import tkinter
import customtkinter
import YouTube
from yt_dlp import DownloadError
from requests import HTTPError


# Downloads YouTube video
def mp3() -> None:
    """This is the function used in the mp3 button call"""
    # Get link from label box
    youtube_link = link.get()
    
    # Informs the user that it is attempting the download of the link
    finish_label.configure(text = 'Attempting to download link')
    
    # Runs the download_mp3 function from YouTube
    try:
        return_str = YouTube.download_mp3(youtube_link)
        finish_label.configure(text = '')
        finish_label.configure(text = return_str)
        
    # Informs the user of any errors has occured when downloading
    except HTTPError:
        finish_label.configure(text = return_str)
        
    except DownloadError:
        finish_label.configure(text = return_str)
    
    except Exception:
        finish_label.configure(text = return_str)
        
        
# Downloads YouTube video
def mp4() -> None:
    """This is the function used in the mp4 button call"""
    # Get link from label box
    youtube_link = link.get()
    
    # Informs the user that it is attempting the download of the link
    finish_label.configure(text = 'Attempting to download link')
    
    # Runs the download_mp3 function from YouTube
    try:
        return_str = YouTube.download_mp4(youtube_link)
        finish_label.configure(text = '')
        finish_label.configure(text = return_str)
        
    # Informs the user of any errors has occured when downloading
    except HTTPError:
        finish_label.configure(text = return_str)
        
    except DownloadError:
        finish_label.configure(text = return_str)
    
    except Exception:
        finish_label.configure(text = return_str)


# Clears text from GUI
def clear() -> None:
    """Clears all display text in the gui"""
    # Creats empty string and replaces the input string
    empty_link = tkinter.StringVar()
    link.configure(textvariable = empty_link)
    
    # Clears label text for user
    finish_label.configure(text = '')


# GUI creation code
if __name__ == '__main__':
    # System Settings
    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme('dark-blue')

    # GUI frame
    app = customtkinter.CTk()
    app.geometry('720x480')
    app.title('YouTube Downloader')

    # UI Elements
    title = customtkinter.CTkLabel(app, text = 'Insert a YouTube link')
    title.pack(padx = 10, pady = 10)

    # Link input
    input_link = tkinter.StringVar()
    link = customtkinter.CTkEntry(app, width = 350, height = 40, textvariable = input_link)
    link.pack()

    # Finished Downloading
    finish_label = customtkinter.CTkLabel(app, text = '')
    finish_label.pack()

    # Download buttons
    button_mp3 = customtkinter.CTkButton(app, text = 'Download MP3', command = mp3)
    button_mp3.pack(padx = 10, pady = 10)
    button_mp4 = customtkinter.CTkButton(app, text = 'Download MP4', command = mp4)
    button_mp4.pack(padx = 10, pady = 10)
    
    # Clear button
    button_clear = customtkinter.CTkButton(app, text = 'Clear', command = clear)
    button_clear.pack(padx = 10, pady = 10)

    # Run GUI
    app.mainloop()
