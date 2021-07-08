import numpy as np
import cv2
file_path = r"C:\\Users\\chenj\\OneDrive\\桌面\\AVSS_E2.avi"
cap = cv2.VideoCapture(file_path)

counter = 0
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == 0:
        break
    frameNo = 'C:/Frames/'+'FrameNo'+str(counter)+'.png'
    counter = counter+1

    cv2.imwrite(frameNo,frame)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
print('frame:', cap.get(cv2.CAP_PROP_FRAME_COUNTER))
print('width:', cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('height:', cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.release()
cv2.destoryAllWindows()