from Init_.until import *

cap = cv2.VideoCapture('/home/quangminh/Desktop/8963058681407290323.mp4')
contrast_threshold=0.05
while True:
    
    # read the current frame
    ret, frame = cap.read()
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
    
