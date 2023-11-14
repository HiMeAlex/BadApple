
import numpy
import cv2, os

cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    term_size = os.get_terminal_size()
    gray = cv2.flip(cv2.resize(cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY), term_size), 1)
    char_list = [i for i in '@%#*+=-:. '][::-1]
    # ['-','/','>','%','@']
    array = numpy.multiply(numpy.divide(numpy.array(gray), 256), len(char_list)-1).astype(int)
    print(''.join([''.join([char_list[j] for j in i]) +'\n' for i in array]).removesuffix('\n'))
    
    # Our operations on the frame come here
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()