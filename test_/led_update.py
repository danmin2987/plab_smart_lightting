from until import *
from DayNight import *

from uart import *
from detection import *
# mo camera
video = cv2.VideoCapture(2)
i_frame = 0
while True :
    global frame
    ret,frame = video.read()
    i_frame +=1  
    if  i_frame%1==0:
        # Thuc hien detect
        frame = do_detect(frame,net,classNames)[0]
    cv2.imshow("frame", frame)
    var = detect_ligh(frame)[0]
    #print(detect_ligh(frame)[2])
    #print(detect_ligh(frame)[1])
    get_serial(var)
    #print (do_detect(frame,net,classNames)[1])
    print(var)
    
    
    
        
    
    

    if cv2.waitKey(1) >= 0:
        break

video.release()

cv2.destroyAllWindows()
