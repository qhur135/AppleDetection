from random import *
import numpy as np
import cv2, os

img_path = "./test/img"
pred_path = "./test/loc"
save_path = "./test/box"


# color
blue = (255,0,0)
green = (0,255,0) # gt
red = (0,0,255)
white = (255,255,255)

img_list = os.listdir(img_path)
#pred_list = os.listdir(pred_path)


# gt bounding box
for i in range(len(img_list)):
    img_name = img_path+'/'+img_list[i]
    save_name = save_path+'/'+img_list[i]

    origin_img = cv2.imread(img_name, cv2.IMREAD_COLOR)
    save_img = cv2.imwrite(save_name,origin_img) # 이미지 복사

    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    pred_file_name = img_list[i].split('.')[0]+".txt"
    loc = open(pred_path + '/' + pred_file_name, 'r')
    lines = loc.readlines()

    k=1
    for line in lines:
        r = randint(0,256)
        g = randint(0,256)
        b = randint(0,256)
        img = cv2.imread(save_name, cv2.IMREAD_COLOR)
        l = line.split(',')
        name = l[0]
        #confidence = round(float(l[1]),2)
        ymin = int(l[1])
        xmin = int(l[2])
        ymax = int(l[3])
        xmax = int(l[4])
        #info=str(k)+" "+name+" "+str(confidence)
        image = cv2.rectangle(np.array(img), (ymin, xmin), (ymax, xmax), (b,g,r), 2)
        #image = cv2.rectangle(image,(xmin-10, ymin-10),(xmax+10,ymax),(b,g,r),-1)
        #image = cv2.putText(image,info,(ymin,xmin-10),cv2.FONT_HERSHEY_PLAIN,1.5,white,2)
        #cv2.imshow('image',image)
        k+=1
        cv2.imwrite(save_name,image)
        cv2.waitKey(0)
