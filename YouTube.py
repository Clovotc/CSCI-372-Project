# This is the first file for creating a youtube downloader using pytube2
# Maison Kasprick - 10/12/2024
# Version 1.0

# Imports
from pytube.download_helper import download_video
from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable, VideoPrivate


# Tests link provided to see if it is a valid YouTube link
def link_validation(test_link: str) -> bool:
    """This function is used to test a link provided that it is indeed a YouTube link.
        The two starting formats for a valid YouTube link are "https://youtu.be/" and "https://www.youtube.com/"

    Args:
        test_link (str): Provided link

    Returns:
        bool: Returns True if the link provided is a valid YouTube link
              Returns False if it is either a short or an expcetion occured
    """
    # Possible YouTube links
    comparative_video = 'https://youtu.be/'
    comparative_video_url = 'https://www.youtube.com/'
    comparative_short = 'https://www.youtube.com/shorts/'

    # Splits test link by '/'
    link_split = test_link.split('/')

    # Attempts to prove the link is a valid YouTube link
    try:
        # Builds link back together to test if it is a normal YouTube video
        comparative_video_link = f'{link_split[0]}//{link_split[2]}/'
        if comparative_video == comparative_video_link or comparative_video_url == comparative_video_link:
            return True

        # Builds link back together to test if it is a YouTube short (Can't download YouTube shorts, yet)
        comparative_short_link = f'{link_split[0]}//{link_split[2]}/{link_split[3]}/'
        if comparative_short == comparative_short_link:
            print('Can not Download YouTube shorts')
            return False
        
    # Informs the user of errors that occured with the link provided
    except VideoPrivate:
        print(f'"{test_link}" is a private video')
        return False
        
    except VideoUnavailable:
        print(f'"{test_link}" is not a avalible')
        return False
        
    except Exception:
        print(f'"{test_link}" is not a YouTube link or ran into an unexpected error')
        return False


# Downloads YouTube video
def single_video_download(youtube_link: str) -> None:
    try:
        download_video(youtube_link)
        
    except Exception:
        print(Exception)
        
    
# Downloads YouTube playlist 
def playlist_download(youtube_link: str) -> None:
    ...
        
        
# Converts YouTube video to what the user wants
def conversion_choice(user_choice: str, youtube_link: str) -> bool:
    """This function is mainly used in execution of this file by itself.
        The two current choices are 1 for playlist and 2 for a single video

    Args:
        user_choice (str): A numeric string between 1 and 2
        youtube_link (str): Provided link

    Returns:
        bool: Returns True if user did not enter a valid choice option
              Returns False if user did enter a valid choice and executes the corrisponding function
    """
    # Check if user selected to download a playlist
    if user_choice == '1':
        playlist_download(youtube_link)
        return False
    
    # Check if user selected to download a single video
    if user_choice == '2':
        single_video_download(youtube_link)
        return False

    # User did not select a either a playlist or a single video option
    print('Not a valid choice')
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
                           'For a playlist enter 1 \n'
                           'For a single video enter 2 \n'
                           'To Quit enter Q \n'
                           'Choice: ')

        # Exits the while loop
        if conversion in ['q','Q']:
            continue_loop = False
            print('Quiting Program')
            
        # Executes the users choice which will set the new boolean for the while loop
        else:
            continue_loop = conversion_choice(conversion, link)
