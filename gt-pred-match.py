import numpy as np
from collections import namedtuple
import glob
from numba import njit
import numpy as np
from tqdm import tqdm
import os

# boxA -> boxGT, botB -> boxPRED
@njit
def intersection_over_union(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    # compute the area of intersection rectangle

    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)  # 겹치는 넓이
    # compute the area of both the prediction and ground-truth
    # rectangles

    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area

    iou = interArea / float(boxAArea + boxBArea - interArea)
    # return the intersection over union value

    return iou

save_dir = "./input/gt-yolok/top35"
gt_dir = "./input/ground-truth"
pred_dir = "./input/onlyapple-yolok/top35"

gt_file = os.listdir(gt_dir)

pred_file = os.listdir(pred_dir)

gt_loc = [0,0,0,0]
idx = 0

#pred = []
#pred.append("20150919_174730_image176.txt")

global max_iou

for pred_txt in pred_file:
    p_txt = open(pred_dir+"/"+pred_txt,"r")
    pred_lines = p_txt.readlines()  
    g_txt = open(gt_dir+"/"+gt_file[idx],"r")
    gt_lines = g_txt.readlines()
    idx+=1
    
    for p_line in pred_lines:
        max_iou = 0
        for gt_line in gt_lines:
            pred = p_line.split(" ")
            boxPRED = pred[2:6]
            boxPRED[3] = boxPRED[3].rstrip("\n")
     
            gt = gt_line.split(" ")
            boxGT = gt[1:5]
            boxGT[3] = boxGT[3].rstrip("\n")
            for i in range(4):
                boxGT[i]=int(boxGT[i])
                boxPRED[i]=int(boxPRED[i])
            #print(np.array(boxGT))            
            IOU = intersection_over_union(np.array(boxGT), np.array(boxPRED))
            if max_iou < IOU:               
               max_iou =IOU
               gt_loc[0]=boxGT

        #print(str(boxPRED)+" "+str(gt_loc[0])+" "+str(max_iou))
        #os.mkdir(save_dir)
        f = open(save_dir+"/"+pred_txt,"a")
        f.write("apple "+str(gt_loc[0][0])+" "+str(gt_loc[0][1])+" "+str(gt_loc[0][2])+" "+str(gt_loc[0][3])+"\n")
        
  





