import numpy as np
import cv2 # pip install opencv-python
from mss import mss
from PIL import Image

bbox = {'top': 100, 'left': 0, 'width': 400, 'height': 300}

sct = mss()

while 1:

    sct_img = sct.grab(bbox)
    cv2.imshow('screen', np.array(sct_img))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break