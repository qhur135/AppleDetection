# -*- coding: utf-8 -*-
import torch
from PIL import Image
import glob
import numpy as np
import os
import cv2

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5x')

'''
# Images
img1 = Image.open('C:/MinneApple/detection.tar/detection/train/images/*')  # PIL image
#img2 = cv2.imread('C:/MinneApple/detection/detection/test/images/dataset1_front_61.png')[:, :, ::-1]  # OpenCV image (BGR to RGB)
imgs = [img1]  # batch of images
'''

ROOT_PATH = './Data/test/images'

for fname in os.listdir(ROOT_PATH):
    # Inference
    images = np.array(Image.open(os.path.join(ROOT_PATH, fname)))
    results = model(images, size=640)  # includes NMS

    # Results
    results.print()
    results.show()  # or .show()

    save_file = './yolov-x.txt'

    with open(save_file,'a') as f:
        f.write(results)
    # results.xyxy[0]  # img1 predictions (tensor)
    # results.pandas().xyxy[0]  # img1 predictions (pandas)
    #
    # if (results.pandas().xyxy[0][results.pandas().xyxy[0]['name'].str.contains('apple')]):
    #
    #     point = []
    #
    #     for i in range(len(results.pandas().xyxy[0])):
    #         x1 = round(results.pandas().xyxy[0].xmax)
    #         y1 = round(results.pandas().xyxy[0].ymax)
    #         x2 = round(results.pandas().xyxy[0].xmin)
    #         y2 = round(results.pandas().xyxy[0].ymin)
    #
    #         point.append([x1.values[i], y1.values[i], x2.values[i], y2.values[i]])
    #
    #         SAVE_FILE = './not_apple_gt_result.txt'
    #         with open(SAVE_FILE, 'a') as f:
    #             f.write(f'{fname},{point[i]}\n')