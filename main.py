# This is the combined code of both GUI and YouTUbe files
# Maison Kasprick - 11/4/2024
# Version 1.0.1

# Imports
import tkinter
import customtkinter
from yt_dlp import YoutubeDL


# Tests link provided to see if it is a valid YouTube link
def link_validation(test_link: str) -> bool:
    """This function is used to test a link provided that it is indeed a YouTube link.
        The two starting formats for a valid YouTube link are "https://youtu.be/" and "https://www.youtube.com/"

    Args:
        test_link (str): Provided link

    Returns:
        bool: Returns True if the link provided is a valid YouTube link
              Returns False if an expcetion occured
    """
    
    # Possible YouTube links
    comparative_video = 'https://youtu.be/'
    comparative_video_url = 'https://www.youtube.com/'

    # First removes any spaces in the link then 
    # Splits test link by '/'
    link_split = test_link.split()
    link_split = test_link.split('/')

    # Attempts to prove the link is a valid YouTube link by
    # Building the link back together to test if it is a normal YouTube video
    comparative_video_link = f'{link_split[0]}//{link_split[2]}/'
    if comparative_video == comparative_video_link or comparative_video_url == comparative_video_link:
        return True
    
    # If the provided link 
    valid_label.configure(f'"{test_link}" is not a valid YouTube link')
    return False


# Downloads YouTube video
def download_mp3() -> None:
    """This is the funcito to download your video or playlist as all mp3 files"""
    # Get link from label box
    youtube_link = link.get()
    
    # Test to see if YouTube link provided is valid
    if link_validation(youtube_link) is False:
        finish_label.configure('Unsuccessful MP3 Download Attempt, Try again.')
        return
    
    # Attempts to download YouTube video if valid
    try:
        download_options = {
            # # # Save location and file name
            # # 'save_location': location + '/%(title)s.%(exts)s', 
            # Post-process to convert to MP3
            'postprocessors': [{ 
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                # '0' means best quality, auto-determined by source
                'preferredquality': '0',
            }],
        }
        # Iterates through the playlist or just downloads the one video
        with YoutubeDL(download_options) as youtube_download:
            youtube_download.download([youtube_link])
            # Refresh finish_label variable
            finish_label.configure(text = '')
            # Inform the user that the download was successful
            finish_label.configure(text = 'Successfully Downloaded MP3 File')
        
    # Informs the user that an error has occured when downloading
    except Exception:
        finish_label.configure(text = f'"{youtube_link}" YouTube video does not exist or was not able to be downloaded')
        
        
# Downloads YouTube video
def download_mp4() -> None:
    """This is the funcito to download your video or playlist as all mp4 files"""
    # Get link from label box
    youtube_link = link.get()
    
    # Test to see if YouTube link provided is valid
    if link_validation(youtube_link) is False:
        valid_label.configure('Unsuccessful MP4 Download Attempt, Try again.')
        return
    
    # Attempts to download YouTube video if valid
    try:
        download_options = {
            # # # Save location and file name
            # # 'save_location': location + '/%(title)s.%(exts)s', 
            # Post-process to convert to MP4
            'postprocessors': [{  
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp4',  
                # '0' means best quality, auto-determined by source
                'preferredquality': '0',
            }],
        }
        # Iterates through the playlist or just downloads the one video
        with YoutubeDL(download_options) as youtube_download:
            youtube_download.download([youtube_link])
            # Refresh finish_label variable
            finish_label.configure(text = '')
            # Inform the user that the download was successful
            finish_label.configure(text = 'Successfully Downloaded MP4 File')
        
    # Informs the user that an error has occured when downloading
    except Exception:
        finish_label.configure(text = f'"{youtube_link}" YouTube video does not exist or was not able to be downloaded')


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
    
    # Not valid link
    valid_label = customtkinter.CTkLabel(app, text = '')
    valid_label.pack()

    # # Progress percentage
    # pPercentage = customtkinter.CTkLabel(app, text = '0%')
    # pPercentage.pack()

    # progressBar = customtkinter.CTkProgressBar(app, width = 400)
    # progressBar.set(0)
    # progressBar.pack(padx = 10, pady =10)

    # Download buttons
    button_mp3 = customtkinter.CTkButton(app, text = 'Download MP3', command = download_mp3)
    button_mp3.pack(padx = 10, pady = 10)
    button_mp4 = customtkinter.CTkButton(app, text = 'Download MP4', command = download_mp4)
    button_mp4.pack(padx = 10, pady = 10)

    # Run GUI
    app.mainloop()
