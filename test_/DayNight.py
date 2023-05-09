from until import *
from detection import *

#****************************************************************************************#
thresold = 110
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
def detect_ligh(frame):
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
    
    #Neu cnt <1 sua chu ky dau bi sai 
    if(cnt<1):
        #Dem so pixel sang va toi
        number_of_white_pix = np.sum(thres == 255)
        number_of_black_pix = np.sum(thres == 0)

        #Tinh ty le tra ve phan tram sang
        a = ty_le(number_of_white_pix,number_of_black_pix)
        
        #print(a)
        if((time_now>morning_5h and time_now<night_18h) ):
            if(a>40):#Neu troi sang
                value = "0"#muc sang thap
                value_uart = "0"
                brigh_level = "high"
            elif(a<4):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "200" #muc sang cao
                value_uart = "3"
                brigh_level = "low"
            elif(a<4 and do_detect(frame,net,classNames)[1] == 15 ):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "255" #muc sang cao
                value_uart = "4"
                brigh_level = "low"
            
            else:
                value = "127"#Muc sang trung binh
                value_uart = "1"
                brigh_level = "medium"
        else:
            #Vi khong duoc tat han den khi troi toi 
            if(a>40):#Neu troi sang
                value = "127"#muc sang trung binh
                value_uart = "1"
                brigh_level = "medium"
            elif(a>40 and do_detect(frame,net,classNames)[1] == 15 ):#Neu troi sang
                value = "170"#muc sang trung binh
                value_uart = "2"
                brigh_level = "medium"
            
            elif(a<11):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "200" #muc sang cao
                value_uart = "3"
                brigh_level = "low"
            elif(a<11 and do_detect(frame,net,classNames)[1] == 15 ):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "255" #muc sang cao
                value_uart = "4"
                brigh_level = "low"
            else:
                value = "170"#Muc sang trung binh
                value_uart = "2"
                brigh_level = "medium"
            cnt += 1
    elif(cnt>0 and cnt <31):
        cnt += 1
    else:
        #Dem so pixel sang va toi
        number_of_white_pix = np.sum(thres == 255)
        number_of_black_pix = np.sum(thres == 0)

        #Tinh ty le
        a = ty_le(number_of_white_pix,number_of_black_pix)
        #print(a)
        if((time_now>morning_5h and time_now<night_18h) ):
            if(a>40):#Neu troi sang
                value = "0"#muc sang thap
                value_uart = "0"
                brigh_level = "high"
            elif(a>40 and do_detect(frame,net,classNames)[1] == 15 ):#Neu troi sang
                value = "170"#muc sang trung binh
                value_uart = "2"
                brigh_level = "medium"
            elif(a<4):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "200" #muc sang cao
                value_uart = "3"
                brigh_level = "low"
            elif(a<4 and do_detect(frame,net,classNames)[1] == 15 ):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "255" #muc sang cao
                value_uart = "4"
                brigh_level = "low"
            
            else:
                value = "127"#Muc sang trung binh
                value_uart = "1"
                brigh_level = "medium"
        else:
            #Vi khong duoc tat han den khi troi toi 
            if(a>40):#Neu troi sang
                value = "127"#muc sang trung binh
                value_uart = "1"
                brigh_level = "medium"
            elif(a>40 and (do_detect(frame,net,classNames)[1] == 15 or do_detect(frame,net,classNames)[1] == 8 or do_detect(frame,net,classNames)[1] == 16 or do_detect(frame,net,classNames)[1] == 5)):#Neu troi sang
                value = "170"#muc sang trung binh
                value_uart = "2"
                brigh_level = "medium"
            
            elif(a<11):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "200" #muc sang cao
                value_uart = "3"
                brigh_level = "low"
            elif(a<11 and do_detect(frame,net,classNames)[1] == 15 ):#Neu troi toi tuy vao muc do toi ta se bat den tuong ung
                value = "255" #muc sang cao
                value_uart = "4"
                brigh_level = "low"
            else:
                value = "170"#Muc sang trung binh
                value_uart = "2"
                brigh_level = "medium"
        cnt = 0
    #Hien thi video
    #opencv color : BGR
    return value_uart,do_detect(frame,net,classNames)[1],a
    
    

# usage: bright_level = detect_ligh(frame)
