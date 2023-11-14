import numpy, cv2, os,threading
from mss import mss
from time import sleep
from PIL import Image as img
from pathlib import Path
frame_list = []

def create_frames(char_list:list = [i for i in'@%#*+=-:. ']):
    global frame_list
    bounding_box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
    char_list = [i for i in " .:-=+*#%@"]
    sct = mss()
    
    while True:
        term_size = tuple(os.get_terminal_size())
        term_size = (term_size[0], term_size[1]-1)
        sct_img = sct.grab(bounding_box)
        array = numpy.array(sct_img)
        gray = cv2.resize(cv2.cvtColor(array, cv2.COLOR_BGR2GRAY), term_size)
        array = numpy.multiply(numpy.divide(numpy.array(gray), 256), len(char_list) - 1).astype(int)
        frame_list.append(''.join([''.join([char_list[j] for j in i]) +'\n' for i in array]).removesuffix('\n'))

def print_frames():
    sleep(.1)
    for i in frame_list:
        sleep(.1)
        print(i)

def main(char_str:str='@%#*+=-:. '):
    char_str = [i for i in char_str][::-1]
    t1 = threading.Thread(target=create_frames, args=())
    t2 = threading.Thread(target=print_frames, args=())
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()
if __name__ == '__main__':
    main()
