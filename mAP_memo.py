import numpy as np
from collections import namedtuple
import cv2
import glob

pred_file = open("C:/MinneApple/yolov5m.txt", 'r')
pred_lines = pred_file.readlines()

path="C:/MinneApple/yolo/"

for pred_line in pred_lines:
    
     name = pred_line.rstrip('\n').split(' ')[:1]
     name=' '.join(name)
     point=pred_line.rstrip('\n').split(' ')[1:]
     point=' '.join(point)
     fru=pred_line.rstrip('\n').split(',')[5:]
     fru=' '.join(fru)
     
     with open(name+'.txt', 'a') as f:
         f.write(f'{point}\n')
     
pred_file.close()
f.close()