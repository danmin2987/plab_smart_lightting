import numpy as np
import argparse
import cv2
import time
from datetime import datetime
import math
import serial
#****************************************************************************************#
thresold = 100
value = ""
#****************************************************************************************#
#Doc time
def timer():
    time_now = datetime.now()
    return time_now
#****************************************************************************************#
#Tinh ty le
def ty_le(white,black):
    ty_le = white/(white+black)
    percent = ty_le*100
    return percent
#****************************************************************************************#
#Phat hien sang toi
def detect_ligh_1(frame):
    cnt=0#bien dem time trich xuat gia tri
    #Covert BGR to GRAY
    
    
        #global frame#khung hinh sau khi xoay 90 do
    ret,frame = video.read()
    x1, y1, x2, y2 = 30,20,200,200
    roi = frame[y1:y2, x1:x2] 
    cv2.imshow('video',roi)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('video1',gray)
    _,thres = cv2.threshold(gray,thresold,255,cv2.THRESH_BINARY)
    if(cnt<1):
        #Dem so pixel sang va toi
        number_of_white_pix = np.sum(thres == 255)
        number_of_black_pix = np.sum(thres == 0)

        #Tinh ty le tra ve phan tram sang
        a = ty_le(number_of_white_pix,number_of_black_pix)
        print(a)
    
    #Hien thi nguong
    cv2.imshow('video2',thres)
video = cv2.VideoCapture('/home/quangminh/Desktop/8963058681407290323.mp4')
while True :
    global frame
    ret,frame = video.read()
         
    cv2.imshow('frame', frame)
    frame = detect_ligh_1(frame)
    if cv2.waitKey(1) >= 0:
        break
