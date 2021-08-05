from random import *
import numpy as np
import cv2, os

img_path = "./img"
save_path = "./box"
pred_path = "./location"


# color
blue = (255,0,0)
green = (0,255,0) # gt
red = (0,0,255)
white = (255,255,255)

img_list = os.listdir(img_path)
pred_list = os.listdir(pred_path)


# gt bounding box
for i in range(len(img_list)):
    img_name = img_path+'/'+img_list[i]
    save_name = save_path+'/'+img_list[i]

    origin_img = cv2.imread(img_name, cv2.IMREAD_COLOR)
    save_img = cv2.imwrite(save_name,origin_img) # 이미지 복사

    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    pred_file_name = pred_list[i]
    loc = open(pred_path + '/' + pred_file_name, 'r')
    lines = loc.readlines()

    k=1
    for line in lines:
        r = randint(0,256)
        g = randint(0,256)
        b = randint(0,256)
        img = cv2.imread(save_name, cv2.IMREAD_COLOR)
        l = line.split(' ')
        name = l[0]
        confidence = l[1]
        ymin = int(l[2])
        xmin = int(l[3])
        ymax = int(l[4])
        xmax = int(l[5])
        info=k+" "+name+" "+confidence
        image = cv2.rectangle(np.array(img), (xmin, ymin), (xmax, ymax), (b,g,r), 2)
        image = cv2.rectangle(image,(xmin-10, ymin-10),(xmax+10,ymax),(b,g,r),-1)
        image = cv2.putText(image,info,(xmin-10,ymin-30),cv2.FONT_HERSHEY_PLAIN,0.6,white,2)
        cv2.imshow('image',image)
        k+=1
        #cv2.imwrite(save_name,image)
        cv2.waitKey(0)