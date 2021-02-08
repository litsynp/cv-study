import numpy as np
import cv2


def write_video():
    """
    Records a video using webcam and saves it in the current working directory.
    """
    try:
        print('Launching the camera.')
        cap = cv2.VideoCapture(0)
    except:
        print('Failed to launch the camera.')
        return

    fps = 20.0
    width = int(cap.get(3))  # frame width
    height = int(cap.get(4))  # frame height

    # Apply DIVX codec
    fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')

    out = cv2.VideoWriter('mycam.avi', fcc, fps, (width, height))
    print('Starts recording now.')

    while True:
        ret, frame = cap.read()

        if not ret:
            print('Error while reading video.')
            break

        cv2.imshow('video', frame)
        out.write(frame)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            print('Stops recording now.')
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


write_video()
