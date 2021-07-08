import numpy as np
import cv2
file_path = r"C:\\Users\\chenj\\OneDrive\\桌面\Warner Brothers Intro HD.mp4"
cap = cv2.VideoCapture(file_path)

counter = 0
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == 0:
        break
    frameNo = 'C:/Frames/'+'FrameNo'+str(counter)+'.png'
# f'{counter}.png'
    cv2.imwrite(frameNo,frame)
    cv2.imshow('frame',frame)
    counter = counter+1

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
print('frame:', cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('width:', cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('height:', cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('fps:', cap.get(cv2.CAP_PROP_FPS))
cap.release()
cv2.destroyAllWindows()