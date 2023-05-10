
from Init_.until import *
parser = argparse.ArgumentParser(description='Use MobileNet SSD on Pi for object detection')
parser.add_argument("--vid_file", help="Duong dan den file video")
parser.add_argument("--prototxt", default="/home/quangminh/Desktop/Plab /led1/Object_Detection_Algorithm/Network_Model_SSD/MobileNetSSD_deploy.prototxt")
parser.add_argument("--weights", default="/home/quangminh/Desktop/Plab /led1/Object_Detection_Algorithm/Network_Model_SSD/MobileNetSSD_deploy.caffemodel")
args = parser.parse_args()

net = cv2.dnn.readNetFromCaffe(args.prototxt, args.weights)
classNames = { 0: 'background',
    1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
    5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
    10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
    14: 'motorbike', 15: 'person', 16: 'pottedplant',
    17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor' }
def color_list(class_id):
    colorList = [ (255, 0, 0),
    (0, 51, 102), (51, 102, 153), (51, 102, 204), (0, 51, 153),
    (0, 102, 102), (0, 102, 153), (102, 255, 153), (128, 0, 0),(255, 255, 0),
    (153, 204, 0), (102, 0, 51), (102, 0, 204), (153, 0, 204),
    (255, 102, 102), (0, 102, 255), (204, 153, 0),
    (204, 204, 255), (255, 255, 153), (255, 80, 80), (102, 153, 153)]
    #Color type
    color_type = colorList[class_id]
    return color_type
def cal_position(detections,i,cols,rows,frame):
    
    # Lay class_id
    class_id = int(detections[0, 0, i, 1])

    # Tinh toan vi tri cua doi tuong
    xLeftBottom = int(detections[0, 0, i, 3] * cols)
    yLeftBottom = int(detections[0, 0, i, 4] * rows)
    xRightTop = int(detections[0, 0, i, 5] * cols)
    yRightTop = int(detections[0, 0, i, 6] * rows)


    heightFactor = frame.shape[0] / 300.0
    widthFactor = frame.shape[1] / 300.0


    xLeftBottom = int(widthFactor * xLeftBottom)
    yLeftBottom = int(heightFactor * yLeftBottom)
    xRightTop = int(widthFactor * xRightTop)
    yRightTop = int(heightFactor * yRightTop)

    return class_id, xLeftBottom, yLeftBottom, xRightTop, yRightTop
class_id = 0       
xLeftBottom = 100
yLeftBottom = 80
xRightTop = 0
yRightTop = 0
def do_detect(frame, net, classNames):
    global xLeftBottom, yLeftBottom,xRightTop, yRightTop,class_id
    # Resize anh ve 300x300
    frame_resized = cv2.resize(frame, (300, 300))

    # Doc blob va dua vao mang predict
    blob = cv2.dnn.blobFromImage(frame_resized, 0.007843, (300, 300), (127.5, 127.5, 127.5), False)
    net.setInput(blob)
    detections = net.forward()

    # Xu ly output cua mang
    cols = frame_resized.shape[1]
    rows = frame_resized.shape[0]

    # Duyet qua cac object detect duoc
    for i in range(detections.shape[2]):
        # Lay gia tri confidence
        confidence = detections[0, 0, i, 2]
        # Neu vuot qua 0.5 threshold
        if confidence > 0.5:

            # Tinh toan vi tri cua doi tuong
            class_id, xLeftBottom, yLeftBottom, xRightTop, yRightTop = cal_position(detections,i, cols,rows,frame)
            
            #Chi ve khung doi voi person, car, bus,bicycle,motorbike,dog,cat
            #if class_id == 2 or class_id == 6 or class_id == 7 or class_id == 8 or class_id == 12 or class_id == 14 or class_id == 15 :
            # Ve khung hinh chu nhat
            cv2.rectangle(frame, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop),  color_list(class_id), 2)

            # Ve label cua doi tuong
            if class_id in classNames:
            
                label = "ID :" + classNames[class_id] 
            
           
                #Ve duong bao ID
                label_size, baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
                # cv2.FILLED la dien day mau trong hinh chu nhat do
                cv2.rectangle(frame,(xLeftBottom , yLeftBottom),(xLeftBottom +160, yLeftBottom+40),color_list(class_id), cv2.FILLED,)
                #Viet ID doi tuong
                cv2.putText(frame, label, (xLeftBottom , yLeftBottom+15), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0))
                cv2.putText(frame, "Toa do : ("+str(xRightTop)+","+str(yRightTop)+")", (xLeftBottom , yLeftBottom + 30), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0))
    #return class_id 
    return frame,class_id
