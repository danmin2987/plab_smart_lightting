import cv2
import numpy as np

# define the minimum brightness difference
BRIGHTNESS_THRESHOLD = 18

# create a video capture object
cap = cv2.VideoCapture('/home/quangminh/Desktop/Plab /mart_lightting_/test_giai_thuat_/video_/5311577521514276025.mp4')

# check if camera opened successfully


# loop through frames
while True:
    # read the current frame
    ret, frame = cap.read()
    x1, y1, x2, y2 = 200,100,500,400
    roi = frame[y1:y2, x1:x2] 
    cv2.imshow('video',roi)
    # check if frame was successfully read
    

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

    # check for quit command
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
