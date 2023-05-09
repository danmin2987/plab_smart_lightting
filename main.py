from Init_.until import *
from Image_Process_Algorithm.DayNight1 import *
from Image_Process_Algorithm.DayNight2 import *
from Protocol_.uart import *
from Object_Detection_Algorithm.Network_Model_SSD.detection import *
# mo camera

def c1():
    video = cv2.VideoCapture(2)
    
    while True :
        #global var2
        global frame#khung hinh sau khi xoay 90 do
        ret,frame = video.read()
        #i_frame +=1  
        #if  i_frame%1==0:
        # Thuc hien detect
        frame = do_detect(frame,net,classNames)[0]
        cv2.imshow("frame", frame)
        var2 = detect_ligh_2(frame)
        queue2.put(var2)
        #get_serial(var)
        #print (do_detect(frame,net,classNames)[1])
        #print(var2)
        
     
        if cv2.waitKey(1) >= 0:
            break
    #c3(var1, var2)
    video.release()

def c2():   
    video_1 = cv2.VideoCapture(0)

    while True :
        #global var1
        global frame_1#khung hinh sau khi xoay 90 do
        ret,frame_1 = video_1.read()
    #i_frame +=1  
    #if  i_frame%1==0:
        # Thuc hien detect
    #frame = do_detect(frame,net,classNames)[0]
        cv2.imshow("frame_1", frame_1)
        var1 = detect_ligh_1(frame_1)
        # get a unit of work
        #queue1.put(var1)
        # check for stop
        #get_serial(var)
    #print (do_detect(frame,net,classNames)[1])
        #rint(var1)
        #print(var2)
        var2 = queue2.get()
        if var1 == "0" and var2 == "6" :
            var = "0"
        if var1 == "1" and var2 == "6" :
            var = "2"
        if var1 == "2" and var2 == "6" :
            var = "3"
        if var1 == "3" and var2 == "6" :
            var = "4"   
        if var1 == "0" and var2 == "5" :
            var = "0"
        if var1 == "1" and var2 == "5" :
            var = "2"
        if var1 == "2" and var2 == "5" :
            var = "3"
        if var1 == "3" and var2 == "5" :
            var = "4"  
        if var1 == "2" and var2 == "8" :
            var = "4"    
        if var1 == "3" and var2 == "7" :
            var = "4" 
        if var1 == "0" and var2 == "0" :
            var = "0" 
        if var1 == "1" and var2 == "0" :
            var = "1" 
        
        if var1 == "2" and var2 == "0" :
            var = "2" 
        if var1 == "3" and var2 == "0" :
            var = "3" 
        get_serial(var)
        print(var)
   
        if cv2.waitKey(1) >= 0:
            break  
    #c3(var1, var2)
    video_1.release()
#cv2.destroyAllWindows()
############################################################################
# 5h sang den 18h

#def c3():
    #while True :
        #var2 = queue2.get()
        #var1 = queue1.get()
        #print(var1)
        #print(var2)

        
        
            
            #print(var)
    #var1 = c2(var1)
    #var2 = c2(var2)
   # while True :
        
        #global var
    cv2.destroyAllWindows()

queue2 = Queue()
tCap1 = multiprocessing.Process(target=c1)
tCap2 = multiprocessing.Process(target=c2)
#tCap3 = multiprocessing.Process(target=c3)
tCap1.start()
tCap2.start()
#tCap3.start()
tCap1.join()
tCap2.join()
#tCap3.join()        



