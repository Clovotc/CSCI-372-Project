# This is the combined code of both GUI and YouTUbe files
# Maison Kasprick - 11/5/2024
# Version 1.0.2

# Imports
import tkinter
import customtkinter
import YouTube


# Downloads YouTube video
def mp3():
    # Get link from label box
    youtube_link = link.get()
    
    # Informs the user that it is attempting the download of the link
    finish_label.configure(text = 'Attempting to download link')
    
    # Runs the download_mp3 function from YouTube
    try:
        return_str = YouTube.download_mp3(youtube_link)
        finish_label.configure(text = '')
        finish_label.configure(text = return_str)
        
    # Informs the user that an error has occured when downloading
    except Exception:
        finish_label.configure(text = return_str)
        
        
# Downloads YouTube video
def mp4() -> None:
    # Get link from label box
    youtube_link = link.get()
    
    # Informs the user that it is attempting the download of the link
    finish_label.configure(text = 'Attempting to download link')
    
    # Runs the download_mp3 function from YouTube
    try:
        return_str = YouTube.download_mp4(youtube_link)
        finish_label.configure(text = '')
        finish_label.configure(text = return_str)
        
    # Informs the user that an error has occured when downloading
    except Exception:
        finish_label.configure(text = return_str)


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

    # # Progress percentage
    # pPercentage = customtkinter.CTkLabel(app, text = '0%')
    # pPercentage.pack()

    # progressBar = customtkinter.CTkProgressBar(app, width = 400)
    # progressBar.set(0)
    # progressBar.pack(padx = 10, pady =10)

    # Download buttons
    button_mp3 = customtkinter.CTkButton(app, text = 'Download MP3', command = mp3)
    button_mp3.pack(padx = 10, pady = 10)
    button_mp4 = customtkinter.CTkButton(app, text = 'Download MP4', command = mp4)
    button_mp4.pack(padx = 10, pady = 10)

    # Run GUI
    app.mainloop()
