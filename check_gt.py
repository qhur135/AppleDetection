import numpy as np
import cv2, os

img_path = "./Data/test/images"
save_path = "./Data/test/test-images"
gt_path = "./Locations/for_get_AP_yx/ground-truth"

# color
blue = (255,0,0)
green = (0,255,0) # gt
red = (0,0,255)

img_list = os.listdir(img_path)
gt_list = os.listdir(gt_path)


# gt bounding box
for i in range(len(img_list)):
    img_name = img_path+'/'+img_list[i]
    save_name = save_path+'/'+img_list[i]

    origin_img = cv2.imread(img_name, cv2.IMREAD_COLOR)
    save_img = cv2.imwrite(save_name,origin_img) # 이미지 복사

    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    gt_file_name = gt_list[i]
    loc = open(gt_path+'/'+gt_file_name,"r")
    lines = loc.readlines()
    for line in lines:
        img = cv2.imread(save_name, cv2.IMREAD_COLOR)
        l = line.split(' ')
        ymin = int(l[1])
        xmin = int(l[2])
        ymax = int(l[3])
        xmax = int(l[4])
        image = cv2.rectangle(np.array(img), (xmin, ymin), (xmax, ymax), green, 3)
        cv2.imwrite(save_name,image)
        cv2.waitKey(0)