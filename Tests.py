# These tests on the files of the project
# Maison Kasprick - 11/5/2024
# Version 1.0.1

# Imports
import YouTube


# YouTube functions tests
def valid_youtube_1() -> bool:
    good_link = 'https://youtu.be/'
    if YouTube.link_validation(good_link):
        return True
    
    return False
    
    
def valid_youtube_2() -> bool:
    good_link = 'https://www.youtube.com/'
    if YouTube.link_validation(good_link):
        return True
    
    return False
    
    
def valid_youtube_3() -> bool:
    bad_link = 'https://yout.be/'
    if YouTube.link_validation(bad_link):
        return True
    
    return False
    
    
def mp3_youtube_1() -> bool:
    good_video = 'https://youtu.be/mCSv5PL53x4'
    result = YouTube.download_mp3(good_video)
    
    if result == 'Successfully Downloaded MP3 File':
        return True
    
    return False
    
    
def mp3_youtube_2() -> bool:
    bad_video = 'https://yo.be/mCSv5PL53x4'
    result = YouTube.download_mp3(bad_video)
    
    if result == f'"{bad_video}" is not a valid YouTube link':
        return True
    
    return False
    
    
def mp3_youtube_3() -> bool:
    error_video = 'https://www.youtube.com/watch?v=enYdAxVcNZA&list=WL'
    result = YouTube.download_mp3(error_video)
    
    if result == f'"{error_video}" YouTube video does not exist or was not able to be downloaded':
        return True
    
    return False
    
    
def mp4_youtube_1() -> bool:
    good_video = 'https://youtu.be/enYdAxVcNZA'
    result = YouTube.download_mp3(good_video)
    
    if result == 'Successfully Downloaded MP4 File':
        return True
    
    return False
    
    
def mp4_youtube_2() -> bool:
    bad_video = 'https://yo.be/enYdAxVcNZA'
    result = YouTube.download_mp3(bad_video)
    
    if result == f'"{bad_video}" is not a valid YouTube link':
        return True
    
    return False


def mp4_youtube_3() -> bool:
    error_video = 'https://www.youtube.com/watch?v=enYdAxVcNZA&list=WL'
    result = YouTube.download_mp3(error_video)
    
    if result == f'"{error_video}" YouTube video does not exist or was not able to be downloaded':
        return True
    
    return False
    

if __name__ == '__main__':
    print('All tests should return true')
    print('Style 1 youtube link: ' + str(valid_youtube_1()))
    print('Style 2 youtube link: ' + str(valid_youtube_2()))
    print('Bad youtube link: ' + str(valid_youtube_3()))
    print('MP3 good youtube video: ' + str(mp3_youtube_1()))
    print('MP3 bad youtube video: ' + str(mp3_youtube_2()))
    print('MP3 error youtube video: ' + str(mp3_youtube_3()))
    print('MP4 good youtube video: ' + str(mp4_youtube_1()))
    print('MP4 bad youtube video: ' + str(mp4_youtube_2()))
    print('MP4 error youtube video: ' + str(mp4_youtube_3()))
