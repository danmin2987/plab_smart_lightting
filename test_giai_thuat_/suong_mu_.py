from Init_.until import *

cap = cv2.VideoCapture(2)
contrast_threshold=0.8
while True:
    
    # read the current frame
    ret, frame = cap.read()
    #x1, y1, x2, y2 = 30,20,200,200
    #roi = frame[y1:y2, x1:x2] 
    cv2.imshow('video',frame)
    # Đọc ảnh và chuyển sang ảnh grayscale
   
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video1',gray_image)
    # Tính toán độ tương phản
    max_val = float(gray_image.max())
    min_val = float(gray_image.min())
    contrast = (max_val - min_val) / (max_val + min_val)
    print(contrast)
    # Kiểm tra độ tương phản và trả về kết quả phát hiện sương mù
    if contrast < contrast_threshold:
        print("suong mu")
    else:
        print("khong co suong mu")
    if cv2.waitKey(1) >= 0:
        break
        
    
