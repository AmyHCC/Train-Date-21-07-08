import numpy as np
import cv2
from matplotlib import pyplot as plt

def videoCapture():
    file_path = r'./Video/AVSS_E2.avi'
    cap = cv2.VideoCapture(file_path)

    counter = 0
    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret == 0:
            break
        frameNo = 'C:/20210708code/Frames/'+'FrameNo'+str(counter)+'.png'
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

def mask():
    pathfile = r'./Frames/FrameNo0.png' #r是read的意思
    imgOriginal = cv2.imread(pathfile)
    cv2.imshow('Original', imgOriginal) #原圖無框線


    width = 720
    height = 576

    #設定框線範圍
    col_interval = 50
    for i in range (0, width, col_interval):
        cv2.line(imgOriginal, (i, 0), (i, height), (255, 255, 0), 2)
        cv2.putText(imgOriginal, '%s'%(i), (i, int(col_interval/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), thickness = 1)
    row_interval = 50
    for i in range (0, height, row_interval):
        cv2.line(imgOriginal, (0, i), (width, i), (255, 255, 0), 2)
        cv2.putText(imgOriginal, '%s'%(i), (int(row_interval/2), i), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), thickness = 1)
    cv2.imshow('Original_line', imgOriginal) #原圖加框線

    #遮罩
    mask = np.zeros(imgOriginal.shape[:2], dtype='uint8')
    cv2.imshow('Mask', mask) #黑色遮罩

    pts = np.array([[280, 80], [0, 300], [0, 500], [700, 500], [700, 80]], np.int32)
    cv2.polylines(imgOriginal, [pts], True, (255, 0, 0), thickness = 2)
    cv2.imshow('AreaOfInterest', imgOriginal) #原圖加框線及範圍
    cv2.fillPoly(mask, [pts], 255, 1)
    cv2.imshow('Masked', mask) #有白色範圍的遮罩

    #合併
    masked = cv2.bitwise_and(imgOriginal, imgOriginal, mask=mask)
    cv2.imshow('MaskedImg', masked) # 合併完的照片

    #使用者好對比的視窗
    plt.figure(figsize = (20, 20))
    plt.subplot(231), plt.imshow(imgOriginal), plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(232), plt.imshow(masked), plt.title('Masked'), plt.xticks([]), plt.yticks([])
    plt.show()

    cv2.waitKey(0)  #0是程式結束完等著，1是先等
    cv2.destroyAllWindows()

mask()