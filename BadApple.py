import math, numpy, os, cProfile, pstats, ctypes, pathlib
from PIL import Image as img

def img2ascii(path):
    scale = 1/3
    init_image = img.open(path).convert('L')
    image = init_image.resize((round(init_image.size[0] * (scale)), round(init_image.size[1] * (scale))))
    char_list = [i for i in "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,\\^`'. "]
    x,y = image.size
    print()
    
    array = numpy.asarray(image)
    index_array = [[round(3*((j)/255))-1 for j in i] for i in array]
    print([print(''.join([char_list[j] for j in i])) for i in index_array])
    
    
def img2ascii_filled(path:str, char_list:list = [i for i in "█@ "[::-1]]) -> str:
    term_size = os.get_terminal_size()
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)
    image = img.open(path).convert('L').resize((term_size[0]-1,term_size[1]))
    array = numpy.array(image)
    image.close()
    return (''.join([''.join([char_list[j] for j in i]) +'\n' for i in [[math.floor((len(char_list)-1) * (j) / 255) for j in i] for i in array]]).removesuffix('\n'))

def clear():
    print(chr(27)+'[2J')

def main():
    clear()
    image_list = os.listdir(f'{pathlib.Path(__file__).parent.resolve()}\\data')
    path = [f'{pathlib.Path(__file__).parent.resolve()}\\data\\{i}' for i in image_list]
    for i in path:
        img2ascii_filled(i)    

if __name__ == '__main__':
    with cProfile.Profile() as pr:
        main()
    
        stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    exit()
