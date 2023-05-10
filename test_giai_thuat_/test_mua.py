from Init_.until import *
from Image_Process_Algorithm.DayNight1 import *


# create a video capture object
cap = cv2.VideoCapture('/home/quangminh/Desktop/83329007015806879(1).mp4')
time_now = timer()
    #Time sang toi
morning_5h = time_now.replace(hour=5, minute=0, second=0, microsecond=0)
night_18h = time_now.replace(hour=18, minute=0, second=0, microsecond=0)
while True:
            # read the current frame
            ret, frame = cap.read()
            a = detect_ligh_1(frame)[1]
            #print(a)
            x1, y1, x2, y2 = 50,0,300,200
            roi = frame[y1:y2, x1:x2] 
            cv2.imshow('video',roi)
            # convert the frame to grayscale
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

                    
            if((time_now>morning_5h and time_now<night_18h)):
                
                if(a<0):
                    # define the minimum brightness difference
                    BRIGHTNESS_THRESHOLD = 40

                    # convert the frame to grayscale
                    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

                    # compute the absolute difference between the current and previous frames
                    if 'previous_gray' in locals():
                        diff = cv2.absdiff(gray, previous_gray)

                        # threshold the difference image
                        _, thresh = cv2.threshold(diff, BRIGHTNESS_THRESHOLD, 255, cv2.THRESH_BINARY)

                        # count the number of white pixels in the thresholded image
                        white_pixels = np.sum(thresh == 255)

                        # if the number of white pixels is greater than a threshold, it is likely raining
                        if white_pixels > 50:
                            print("troi mua")
                        else:
                            print("troi khong mua")
            

                        # display the thresholded image
                        cv2.imshow('Threshold', thresh)

                    # set the current frame as the previous frame for the next iteration
                    previous_gray = gray

                    # display the original frame
                    cv2.imshow('Original', frame)
           
            else:
                # define the minimum brightness difference
                BRIGHTNESS_THRESHOLD = 18
                

                # compute the absolute difference between the current and previous frames
                if 'previous_gray' in locals():
                    diff = cv2.absdiff(gray, previous_gray)

                    # threshold the difference image
                    _, thresh = cv2.threshold(diff, BRIGHTNESS_THRESHOLD, 255, cv2.THRESH_BINARY)
    
                    # count the number of white pixels in the thresholded image
                    white_pixels = np.sum(thresh == 255)

                    # if the number of white pixels is greater than a threshold, it is likely raining
                    if white_pixels > 50:
                        print("troi mua")
                    else:
                        print("troi khong mua")
            

                    # display the thresholded image
                    cv2.imshow('Threshold', thresh)

                # set the current frame as the previous frame for the next iteration
                previous_gray = gray

                # display the original frame
                cv2.imshow('Original', frame)
                
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()
