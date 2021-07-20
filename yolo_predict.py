# -*- coding: utf-8 -*-
import torch
from PIL import Image
import glob
import numpy as np
import os
import cv2
import pandas as pd

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
    # results.show()  # or .show()
    # results.save()

    save_file = './yolo-x.csv'

    results = results.pandas().xyxy[0]  # img1 predictions (pandas)

    results.to_csv(f'./result/{fname.split(".")[0]}.csv', sep=' ', float_format="%.6f",
                   columns=["name", "confidence", "ymin", "xmin", "ymax", "xmax"], index=False)

