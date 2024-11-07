# These tests on the files of the project
# Maison Kasprick - 11/6/2024
# Version 1.0.2

# Imports
import YouTube


# YouTube functions tests
def valid_style1() -> bool:
    good_link = 'https://youtu.be/'
    
    if YouTube.link_validation(good_link):
        print(u'\u2713')
        return True 
    
    print('X')
    return False
    
    
def valid_style2() -> bool:
    good_link = 'https://www.youtube.com/'
    
    if YouTube.link_validation(good_link):
        print(u'\u2713')
        return True
    
    print('X')
    return False
    
    
def valid_bad() -> bool:
    bad_link = 'https://yout.be/'
    
    if YouTube.link_validation(bad_link) is False:
        print(u'\u2713')
        return True
    
    print('X')
    return False
    
    
def mp3_good() -> bool:
    good_video = 'https://youtu.be/mCSv5PL53x4'
    
    try:
        result = YouTube.download_mp3(good_video)
        
        if result == 'Successfully Downloaded MP3 File':
            print(u'\u2713')
            return True
        
        print('X')
        return False
    
    except:
        print('X')
        return False
    
    
def mp3_bad() -> bool:
    bad_video = 'https://yo.be/mCSv5PL53x4'
    
    try:
        result = YouTube.download_mp3(bad_video)
        
        if result == '"https://yo.be/mCSv5PL53x4" is not a valid YouTube link':
            print(u'\u2713')
            return True
        
        print('X')
        return False
    
    except:
        print('X')
        return False
    
 
def mp3_error() -> bool:
    error_video = 'https://www.youtube.com/'

    try:
        YouTube.download_mp3(error_video)
    
        print('X')
        return False
    
    except:
        print(u'\u2713')
        return True
    

def mp4_good() -> bool:
    good_video = 'https://youtu.be/enYdAxVcNZA'
    
    try:
        result = YouTube.download_mp4(good_video)
        
        if result == 'Successfully Downloaded MP4 File':
            print(u'\u2713')
            return True
    
        print('X')
        return False
    
    except:
        print('X')
        return False
    
    
def mp4_bad() -> bool:
    bad_video = 'https://yo.be/enYdAxVcNZA'
    
    try:
        result = YouTube.download_mp4(bad_video)
        
        if result == '"https://yo.be/enYdAxVcNZA" is not a valid YouTube link':
            print(u'\u2713')
            return True
    
        print('X')
        return False
    
    except:
        print('X')
        return False


def mp4_error() -> bool:
    error_video = 'https://www.youtube.com/'
    
    try:
        YouTube.download_mp4(error_video)

        print('X')
        return False
    
    except:
        print(u'\u2713')
        return True
    

if __name__ == '__main__':
    print('All tests should return true')
    print('Style 1 youtube link: ' + str(valid_style1()))
    print('Style 2 youtube link: ' + str(valid_style2()))
    print('Bad youtube link: ' + str(valid_bad()))
    print('MP3 good youtube video: ' + str(mp3_good()))
    print('MP3 bad youtube video: ' + str(mp3_bad()))
    print('MP3 error youtube video: ' + str(mp3_error()))
    print('MP4 good youtube video: ' + str(mp4_good()))
    print('MP4 bad youtube video: ' + str(mp4_bad()))
    print('MP4 error youtube video: ' + str(mp4_error()))
