from Init_.until import *
from Object_Detection_Algorithm.Network_Model_SSD.detection import *
#****************************************************************************************#
thresold = 150
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
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('video1',hsv)
    _,thres = cv2.threshold(gray,thresold,255,cv2.THRESH_BINARY)
    #Hien thi nguong
    #cv2.imshow('video2',thres)

    #Doc thi time
    time_now = timer()
    #Time sang toi
    morning_5h = time_now.replace(hour=5, minute=0, second=0, microsecond=0)
    night_18h = time_now.replace(hour=18, minute=0, second=0, microsecond=0)
    night_19h = time_now.replace(hour=19, minute=0, second=0, microsecond=0)
    night_00h = time_now.replace(hour=0, minute=0, second=0, microsecond=0)
    night_23h59p = time_now.replace(hour=23, minute=59, second=59, microsecond=0)
    
    #Neu cnt <1 sua chu ky dau bi sai 
    if(cnt<1):
        #Dem so pixel sang va toi
        number_of_white_pix = np.sum(thres == 255)
        number_of_black_pix = np.sum(thres == 0)

        #Tinh ty le tra ve phan tram sang
        a = ty_le(number_of_white_pix,number_of_black_pix)
        #print(a)
        if((time_now>morning_5h and time_now<night_18h) ):
            if(a>12.8):#Neu troi sang
                value = "0"#muc sang thap
                value_uart = "0"
                brigh_level = "high"
            elif(a<1.6 ):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "200" #muc sang trung binh 
                value_uart = "3"
                brigh_level = "medium"
            elif(a<4.4):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "150" #muc sang cao
                value_uart = "2"
                brigh_level = "medium"
            else:
                value = "127"#Muc sang trung binh
                value_uart = "1"
                brigh_level = "medium"
        if((time_now>night_18h and time_now<night_19h) ):
            if(a>12.8):#Neu troi sang
                value = "0"#muc sang thap
                value_uart = "0"
                brigh_level = "high"
            elif(a<1.6 ):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "200" #muc sang trung binh 
                value_uart = "3"
                brigh_level = "medium"
            elif(a<4.4):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "150" #muc sang cao
                value_uart = "2"
                brigh_level = "medium"
            else:
                value = "127"#Muc sang trung binh
                value_uart = "1"
                brigh_level = "medium"
        if((time_now>night_19h and time_now<night_23h59p) ):
                value = "200" #muc sang trung binh 
                value_uart = "3"
                brigh_level = "medium"
        if((time_now>night_00h and time_now<morning_5h) ):      
                value = "150" #muc sang trung binh 
                value_uart = "2"
                brigh_level = "medium"
        cnt += 1
    elif(cnt>0 and cnt <31):
        cnt += 1
    else:
        number_of_white_pix = np.sum(thres == 255)
        number_of_black_pix = np.sum(thres == 0)

        #Tinh ty le tra ve phan tram sang
        a = ty_le(number_of_white_pix,number_of_black_pix)
        #print(a)
        if((time_now>morning_5h and time_now<night_18h) ):
            if(a>12.8):#Neu troi sang
                value = "0"#muc sang thap
                value_uart = "0"
                brigh_level = "high"
            elif(a<1.6 ):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "200" #muc sang trung binh 
                value_uart = "3"
                brigh_level = "medium"
            elif(a<4.4):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "150" #muc sang cao
                value_uart = "2"
                brigh_level = "medium"
            else:
                value = "127"#Muc sang trung binh
                value_uart = "1"
                brigh_level = "medium"
        if((time_now>night_18h and time_now<night_19h) ):
            if(a>12.8):#Neu troi sang
                value = "0"#muc sang thap
                value_uart = "0"
                brigh_level = "high"
            elif(a<1.6 ):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "200" #muc sang trung binh 
                value_uart = "3"
                brigh_level = "medium"
            elif(a<4.4):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "150" #muc sang cao
                value_uart = "2"
                brigh_level = "medium"
            else:
                value = "127"#Muc sang trung binh
                value_uart = "1"
                brigh_level = "medium"
        if((time_now>night_19h and time_now<night_23h59p) ):
                value = "200" #muc sang trung binh 
                value_uart = "3"
                brigh_level = "medium"
        if((time_now>night_00h and time_now<morning_5h) ):      
                value = "150" #muc sang trung binh 
                value_uart = "2"
                brigh_level = "medium"
            
        cnt = 0
    #Hien thi video
    #opencv color : BGR
    return value_uart, a

# usage: bright_level = detect_ligh(frame)
