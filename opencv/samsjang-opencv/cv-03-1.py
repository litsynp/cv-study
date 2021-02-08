import numpy as np
import cv2


def show_video():
    """
    Creates a window that displays webcam video in grayscale.
    """
    try:
        print('Launching the camera.')
        cap = cv2.VideoCapture(0)
    except:
        print('Failed to launch the camera.')
        return

    cap.set(3, 480)
    cap.set(4, 320)

    while True:
        ret, frame = cap.read()

        if not ret:
            print('Failed to read video')
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('video', gray)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


show_video()
