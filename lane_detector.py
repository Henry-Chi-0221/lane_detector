import cv2
import numpy as np
import math

cap = cv2.VideoCapture('Demo.mp4')


def top_hat(val , size):
    morph_size = size
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*morph_size + 1, 2*morph_size+1), (morph_size, morph_size))
    dst = cv2.morphologyEx(val, cv2.MORPH_TOPHAT, element)
    return dst

while(cap.isOpened()):
    ret , frame = cap.read()
    if (ret == False):
        cap = cv2.VideoCapture('Demo.mp4')
        ret , frame = cap.read()
    
    src = frame[400: ,:]
    gray = cv2.cvtColor(src , cv2.COLOR_BGR2GRAY)
    ret , thres = cv2.threshold(gray , 140, 160,0)
    cv2.imshow('threshold' , thres)
    #thres = cv2.inRange(src ,(0,0,0),(100,360,100))
    thres = cv2.blur(thres, (3,3))
    
    black_bg = np.zeros([720,1280],np.uint8)
    k = cv2.bitwise_or( thres , black_bg[400:,:])
    black_bg[400:,:] = k
    
    #print(black_bg[:320,:].shape == thres.shape)
    cv2.imshow('origin_size_treshold' , black_bg)
    edge_thres = 50
    detected_edges = cv2.Canny(thres, edge_thres, 3*edge_thres, 3 , 3)
    detected_edges = top_hat(detected_edges , 3)
    cv2.imshow('edges'  , detected_edges)

    cdst = cv2.cvtColor(detected_edges, cv2.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)
    linesP = cv2.HoughLinesP(detected_edges, 1, np.pi / 180, 1, None, 10, 10)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)
            dx = l[2] - l[0]
            dy = l[3] - l[1]
            
            #compute slope
            if(dx != 0):
                #print("dy/dx : " , dy/dx)
                if(abs(dy/dx) >0.2 and abs(dy/dx)< 1):
                    length = math.sqrt(math.pow(dx,2) + math.pow(dy,2))
                    if length>10 :
                        cv2.line(frame, (l[0], l[1]+400), (l[2], l[3]+400), (0,0,255), 3, cv2.LINE_AA)
                        #print("arc length : " , length)
    cv2.imshow('src' , frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
