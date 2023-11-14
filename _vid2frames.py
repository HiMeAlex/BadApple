import cv2
import os
import shutil
from pathlib import Path
# Read the video from specified path
def _vid2frames(video):
    cam = cv2.VideoCapture(video)
    
    try:
        # creating a folder named data
        if os.path.exists('data'):
            shutil.rmtree('data')
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        # if not created then raise error
        print ('Error: Creating directory of data')

    currentframe = 0
    
    while True:
        
        # reading from frame
        ret,frame = cam.read()
    
        if ret:
            lead_curframe = f'{currentframe:04}'
            # if video is still left continue creating images
            name = './data/frame' + str(lead_curframe) + '.jpg'
            print ('Creating...' + name)
    
            # writing the extracted images
            cv2.imwrite(name, frame)
    
            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
    
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    vid_list = os.listdir(f'{Path(__file__).parent.absolute()}/Videos')

    while True:
        inp = input(f'please input which video you would like(1-{len(vid_list)}): ')

        if inp.isnumeric() and 1 <= int(inp) <= len(vid_list):
            num = int(inp)
            _vid2frames(f'{Path(__file__).parent.absolute()}/Videos/{vid_list[num-1]}')
            break
        else:
            print('input is either not a number or is not within range.')