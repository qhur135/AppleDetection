import numpy as np
import os
from PIL import Image
from numba import njit

ROOT_PATH = './Data/test/masks'
SAVE_FILE = './gt_location.txt'
cnt = 0

@njit
def solve():
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

                with open(SAVE_FILE, 'a') as f:
                    f.write(f'{file},{ymin},{xmin},{ymax},{xmax}\n')
            else:
                print(f'continue from {file}')


solve()