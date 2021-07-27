import numpy as np
from collections import namedtuple
import glob
from numba import njit
import numpy as np
from tqdm import tqdm

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


gt_file = open("./Locations/gt.txt", 'r')
gt_lines = np.array(sorted(gt_file.readlines()))

pred_file = open("./Locations/rcnn_pred.txt", 'r')
pred_lines = np.array(sorted(pred_file.readlines()))

gt_loc = []
pred_loc= []


def solve(threshold):
    recall_top = 0
    precision_top = 0

    gt_map = dict()
    pred_map = dict()

    # filename : key , locations : value
    for gt_line in gt_lines:
        gt_name = gt_line.split(',')[0]
        if gt_name in gt_map:
            gt_map[gt_name].append(gt_line)
        else:
            gt_map[gt_name] = [gt_line]

    for pred_line in pred_lines:
        pred_name = pred_line.split(',')[0]
        if pred_name in pred_map:
            pred_map[pred_name].append(pred_line)
        else:
            pred_map[pred_name] = [pred_line]

    for gt_line in tqdm(gt_lines):
        max_iou = 0
        boxGT_check = gt_line.rstrip('\n').split(',')[0]
        boxGT = gt_line.rstrip('\n').split(',')[1:] # location : ymin,xmin,ymax,xmax
        boxGT = list(map(int, boxGT))
        #gt_loc.append(boxGT)

        # find maximum value of IOU
        flag = False
        out = False
        for pred_line in pred_map[boxGT_check]:
            boxPRED_check = pred_line.split(',')[0]
            boxPRED = pred_line.split(',')[1:5] # xmin, ymin, xmax, ymax
            boxPRED = list(map(int, boxPRED))

            if boxGT_check == boxPRED_check:
                flag = True
                IOU = intersection_over_union(np.array(boxGT), np.array(boxPRED))
                max_iou = max(max_iou, IOU)
            elif flag:
                break

        if max_iou >= threshold:  # 겹치는 부분이 50% 이상
            recall_top += 1
        # else:
        #     fp += 1

    for pred_line in tqdm(pred_lines):
        max_iou = 0
        boxPRED_check = gt_line.rstrip('\n').split(',')[0]
        boxPRED = gt_line.rstrip('\n').split(',')[1:5]
        boxPRED = list(map(int, boxPRED))
        # gt_loc.append(boxGT)

        # find maximum value of IOU0
        flag = False
        for gt_line in gt_map[boxPRED_check]:
            boxGT_check = gt_line.split(',')[0]
            boxGT = gt_line.split(',')[1:]
            boxGT = list(map(int, boxGT))

            if boxGT_check == boxPRED_check:
                flag = True
                IOU = intersection_over_union(np.array(boxGT), np.array(boxPRED))
                max_iou = max(max_iou, IOU)
            elif flag:
                break

        if max_iou >= threshold:  # 겹치는 부분이 50% 이상
            print(max_iou)
            precision_top += 1



    return np.round((recall_top / len(gt_lines)) * 100, 3), np.round((precision_top/len(pred_lines))*100,3)


# precision, recall = solve(np.round(0.5, 2))
# print(precision, recall)
for threshold in np.arange(0.0, 1.1, 0.1):
    print(f'\n—— threshold : {threshold} ——')
    recall, precision = solve(np.round(threshold, 2))
    print(f'recall: {recall}%, precision: {precision}%\n') # TODO: precision 다시 구하기