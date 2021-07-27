import numpy as np
import cv2, os

img_path = "./Data/test/images"
save_path = "./yolov5l-boundingbox" # option
rcnn_path = "./Locations/for_get_AP_yx/rcnn-results"
yolo_path = "./Locations/for_get_AP_yx/yolov5l-results"

# color
blue = (255,0,0) # yolov5l
green = (0,255,0) # gt
red = (0,0,255) # predict rcnn

img_list = os.listdir(img_path)
predict_list = os.listdir(yolo_path) # option


# rcnn-predict bounding box
for i in range(len(img_list)):
    img_name = img_path+'/'+img_list[i]
    save_name = save_path+'/'+img_list[i]

    origin_img = cv2.imread(img_name, cv2.IMREAD_COLOR)
    save_img = cv2.imwrite(save_name,origin_img) # 이미지 복사

    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    pred_file_name = predict_list[i]
    loc = open(yolo_path+'/'+pred_file_name,"r") #option
    lines = loc.readlines()
    for line in lines:
        img = cv2.imread(save_name, cv2.IMREAD_COLOR)
        l = line.split(' ')
        ymin = int(l[2])
        xmin = int(l[3])
        ymax = int(l[4])
        xmax = int(l[5])
        image = cv2.rectangle(np.array(img), (ymin, xmin), (ymax, xmax), blue, 3)
        cv2.imwrite(save_name,image)
        cv2.waitKey(0)