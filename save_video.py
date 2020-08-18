import numpy as np
import cv2 as cv
import time

timestr = time.strftime("%Y%m%d-%H%M%S")
cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
filename = r'video\output-{}.avi'.format(timestr)
out = cv.VideoWriter(filename, fourcc, 20.0, (640,  480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # write the frame
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
print('Saving file: {}'.format(filename))
out.release()
cv.destroyAllWindows()