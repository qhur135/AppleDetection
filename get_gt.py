import numpy as np
import os
from PIL import Image
from numba import njit

ROOT_PATH = "./Data/train/masks"
SAVE_PATH = "./Locations/for_get_AP_yx/train-gt"
cnt=0


for file in os.listdir(ROOT_PATH):
    im = np.array(Image.open(os.path.join(ROOT_PATH, file)))

    target = np.max(im)
    for label in range(1, target + 1):
        x, y = np.where(im == label)
        if x.tolist() and y.tolist():
            xmin = np.min(x)
            xmax = np.max(x)
            ymin = np.min(y)
            ymax = np.max(y)
                
            save = SAVE_PATH +'/' +file.split('.')[0]+'.txt'
            with open(save, 'a') as f:
                f.write(f'47,{ymin},{xmin},{ymax},{xmax}\n')

        else:
            print(f'continue from {file}')

