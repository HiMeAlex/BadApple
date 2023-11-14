import threading
from time import sleep
import numpy
import os
from PIL import Image as img
from pathlib import Path
import math
import cv2
frame_list = []

def create_frames(char_list:list, size:tuple):
    global frame_list
    file_directory = Path(__file__).parent.absolute()
    image_list = os.listdir(f'{file_directory}/data')
    image_list.sort()
    path_list = [f'{file_directory}/data/{i}' for i in image_list]
    char_list = [i for i in char_list]
    idk = len(char_list)-1

    color_list = ['\33[91m', '\33[93m', '\33[92m', '\33[96m', '\33[94m', '\33[95m']
    for path in path_list:
        image = img.open(path).resize(size)
        gray = image.convert('L')
        gray_array = numpy.multiply(numpy.divide(numpy.array(gray), 256), idk).astype(int)
        image_array = numpy.array(image)
        gray_array =([[str(char_list[j]) for j in i] for i in gray_array])
        color_array = [[color_list[math.floor(numpy.sum(numpy.array([pixel[j]+(j*256) for j in range(3)]))/3/768*len(color_list)-1)] for pixel in row] for row in image_array]

        combined = numpy.hstack((gray_array, color_array))
        print(''.join([''.join([''.join((row[pixel],row[pixel+int(len(row)/2)])) for pixel in range(int(len(row)/2))]) for row in combined]))
        
def print_frames():
    sleep(.1)
    for i in frame_list:
        print(i)

def main(char_str:str='@%#*+=-:. ', size:tuple=os.get_terminal_size()):
    char_str = [i for i in char_str][::-1]
    t1 = threading.Thread(target=create_frames, args=(char_str, size))
    t2 = threading.Thread(target=print_frames, args=())
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == '__main__':
    confirm_1 = input("Would you like a custom character list? (y/n): ").lower()
    confirm_2 = input("would you like to choose a size? (y/n): ").lower()
    
    if confirm_1 == 'y' and confirm_2 == 'y':
        char_str = input("Please type a character set (H -> L brightness): ")
        size_x = input("input the number of cols: ")
        size_y = input("input the number of rows: ")
        if size_x.isdigit() and size_y.isdigit():
            size = (int(size_x), int(size_y))
        main(char_str, size)
    if confirm_1 == 'y':
        char_str = input("Please type a character set (H -> L brightness): ")
        main(char_str)
    if confirm_2 == 'y':
        size_x = input("input the number of cols: ")
        size_y = input("input the number of rows: ")
        if size_x.isdigit() and size_y.isdigit():
            size = (int(size_x), int(size_y))
        main(size=size)
    else:
        main()
    
    print('Finished!')