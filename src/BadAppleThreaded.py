import threading, numpy, os
from time import sleep
from PIL import Image as img
from pathlib import Path
frame_list = []

def create_frames(char_list:list, size:tuple):
    global frame_list
    file_directory = Path(__file__).parent.parent.resolve()
    image_list = os.listdir(f"{file_directory}/data")
    image_list.sort()
    path_list = [f"{file_directory}/data/{i}" for i in image_list]
    path_list.remove(f"{file_directory}/data/generated_frames_go_here.txt")
    char_list = [i for i in char_list]
    for path in path_list:
        gray = img.open(path).resize(size).convert('L')
        array = numpy.multiply(numpy.divide(numpy.array(gray), 256), len(char_list)).astype(int)
        frame_list.append(''.join([''.join([char_list[j] for j in i]) +'\n' for i in array]).removesuffix('\n'))

def print_frames():
    sleep(.1)
    for i in frame_list:
        sleep(.015)
        print(i)

def main(char_str:str="@%#*+=-:. ", size:tuple=os.get_terminal_size()):
    char_str = [i for i in char_str][::-1]
    t1 = threading.Thread(target=create_frames, args=(char_str, size))
    t2 = threading.Thread(target=print_frames, args=())
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    confirm_1 = input("Would you like a custom character list? (y/n): ").lower()
    confirm_2 = input("Would you like to choose a size? (y/n): ").lower()

    if confirm_1 == 'y' and confirm_2 == 'y':
        char_str = input("Please type a character set (H -> L brightness): ")
        size_x = input("input the number of cols: ")
        size_y = input("input the number of rows: ")
        if size_x.isdigit() and size_y.isdigit():
            size = (int(size_x), int(size_y))
        main(char_str, size)
    elif confirm_1 == 'y':
        char_str = input("Please type a character set (H -> L brightness): ")
        main(char_str)
    elif confirm_2 == 'y':
        size_x = input("input the number of cols: ")
        size_y = input("input the number of rows: ")
        if size_x.isdigit() and size_y.isdigit():
            size = (int(size_x), int(size_y))
        main(size=size)
    else:
        main()
    
    print("Finished!")
