__author__ = 'nocte55is@gmail.com'

import cv2


def show_image():
    imgfile = 'images/british-shorthair-cat.png'

    # cv2.imread()
    # 1st param: location of the file you wanna read
    # 2nd param: Flag that decides how to read the image
    # cv2.IMREAD_COLOR: Color / ignores transparency / Default / 1 in int
    # cv2.IMREAD_GRAYSCALE: Grayscale / 0 in int
    # cv2.IMREAD_UNCHANGED: Uses "alpha channel" / -1 in int
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

    # Make the window resizable
    cv2.namedWindow('british-shorthair-cat', cv2.WINDOW_NORMAL)
    cv2.imshow('british-shorthair-cat', img)

    k = cv2.waitKey(0) & 0xFF

    if k == 27:
        # Close the window if a key is pressed other than 'c'
        cv2.destroyAllWindows()
    elif k == ord('c'):
        # Create a copy of the original image if 'c' pressed
        cv2.imwrite('images/british-shorthair-cat-copy.png', img)
        cv2.destroyAllWindows()


show_image()
