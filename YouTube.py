# This is the first file for creating a youtube downloader using pytube2
# Maison Kasprick - 10/11/2024
# Version 1.0

# Imports
from pytube.download_helper import download_video
from pytube import YouTube


# Tests link provided to see if it is a valid YouTube link
def link_validation(test_link: str) -> bool:
    comparative_video = 'https://youtu.be/'
    comparative_video_url = 'https://www.youtube.com/'
    comparative_short = 'https://www.youtube.com/shorts/'

    # Splits test link by '/'
    link_split = test_link.split('/')

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
        
    except Exception:
        print(f'"{test_link}" is not a YouTube link')
        return False


def download(youtube_link: str) -> None:
    try:
        download_video(youtube_link)
        
    except Exception:
        print(Exception)
        
        
# Converts YouTube video to what the user wants
def conversion_choice(user_choice: str, youtube_link: str) -> bool:
    if user_choice == '1':
    #     download_playlist(youtube_link)
        return False
    
    if user_choice == '2':
    #     download_mp4(youtube_link)
        return False
    
    if user_choice == '3':
    #     download_mp3(youtube_link)
        return False
    
    if user_choice == '4':
    #     download_mp4(youtube_link)
    #     download_mp3(youtube_link)
        return False

    print('Not a valid choice')
    return True
        
        
# Gets YouTube link from user and converts to whatever the user wants
def main() -> None:
    print('Note - if you are wanting to download a playlist you will need to copy the search bar url')
    link = input('Paste YouTube link: ')

    # continue_loop = True

    # while continue_loop:
    #     conversion = input('What would you like to do with the link? \n'
    #                        'If it is a Playlist press 1 \n'
    #                        'Download video as MP4 press 2 \n'
    #                        'Download video as MP3 press 3 \n'
    #                        'Download video as Both press 4 \n'
    #                        'To Quit press Q \n'
    #                        'Choice: ')

    #     if conversion in ['q','Q']:
    #         continue_loop = False
    #         print('Quiting Program')
            
    #     else:
    #         continue_loop = conversion_choice(conversion, link)
    
    if link_validation(link):
        print('This is a valid YouTube link')
    
    
# This is what will run if this file is selected
if __name__ == '__main__':
    main()
