# This is the first file for creating a youtube downloader using yt_dlp
# Maison Kasprick - 11/5/2024
# Version 1.0.3

# Imports
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
    
    # If the provided link is not valid
    return False


# Downloads YouTube video
def download_mp3(youtube_link: str) -> str:
    """This is the function to download your video or playlist as all mp3 files

    Args:
        youtube_link (str): Provided YouTube link

    Returns:
        str: Returns the string of either a successful download or unsuccessful download 
    """
    # Test to see if YouTube link provided is valid
    if link_validation(youtube_link) is False:
        return(f'"{youtube_link}" is not a valid YouTube link')
    
    # Attempts to download YouTube video if valid
    try:
        download_options = {
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
            return('Successfully Downloaded MP3 File')
        
    # Informs the user that an error has occured when downloading
    except Exception:
        return(f'"{youtube_link}" YouTube video does not exist or was not able to be downloaded')
        
        
# Downloads YouTube video
def download_mp4(youtube_link: str) -> str:
    """This is the function to download your video or playlist as all mp4 files
    
    Args:
        youtube_link (str): Provided YouTube link

    Returns:
        str: Returns the string of either a successful download or unsuccessful download 
    """
    # Test to see if YouTube link provided is valid
    if link_validation(youtube_link) is False:
        return(f'"{youtube_link}" is not a valid YouTube link')
    
    # Attempts to download YouTube video if valid
    try:
        download_options = {
            # # Post-process to convert to best format
            # 'postprocessors': [{  
            #     'key': 'FFmpegVideoConvertor',
            # }],
        }
        # Iterates through the playlist or just downloads the one video
        with YoutubeDL(download_options) as youtube_download:
            youtube_download.download([youtube_link])
            return('Successfully Downloaded MP4 File')
        
    # Informs the user that an error has occured when downloading
    except Exception:
        return(f'"{youtube_link}" YouTube video does not exist or was not able to be downloaded')
        
        
# Converts YouTube video to what the user wants
def conversion_choice(user_choice: str, youtube_link: str) -> bool:
    """This function is mainly used in execution of this file by itself.
        The two current choices are 1 for mp3 and 2 for mp4

    Args:
        user_choice (str): A numeric string between 1 and 2
        youtube_link (str): Provided link

    Returns:
        bool: Returns True if user did not enter a valid choice option
              Returns False if user did enter a valid choice and executes the corrisponding function
    """
    
    # Check if user selected to download mp3
    if user_choice == '1':
        print(download_mp3(youtube_link))
        return False
    
    # Check if user selected to download mp4
    if user_choice == '2':
        print(download_mp4(youtube_link))
        return False

    # User did not select a either a playlist or a single video option
    print('Not a valid choice \n')
    return True
    
    
# This is what will run if this file is selected
if __name__ == '__main__':
    # Gets YouTube link from user and converts to whatever the user wants
    print('Note - if you are wanting to download a playlist you will need to copy the search bar url')
    link = input('Paste YouTube link: ')

    # Starts a while loop until user enters correct inputs
    continue_loop = True

    while continue_loop:
        conversion = input('What would you like to do with the link? \n'
                           'For a mp3 video enter 1 \n'
                           'For a mp4 video enter 2 \n'
                           'To Quit enter Q \n'
                           'Choice: ')

        # Exits the while loop
        if conversion in ['q','Q']:
            continue_loop = False
            print('Quiting Program')
            
        # Executes the users choice which will set the new boolean for the while loop
        else:
            continue_loop = conversion_choice(conversion, link)
