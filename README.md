# MinneApple Detection

MinneApple dataset을 이용해서 사과를 감지

- frcnn, yolov5 사용
- test 데이터 기존의 test 데이터 사용하지 않고 train에서 랜덤으로 25% 선택함 (기존의 test 데이터에는 mask가 없기 때문)



## Locations 저장 순서 
- Locations 저장 순서(y,x) [ ymin, xmin, ymax, xmax ] 
  -> yolov5 예측 좌표, rcnn 예측 좌표, gt 좌표 저장되어 있음 




# TODO_List
- yolov5 성능 향상을 위해 예측할 때 이미지의 크기를 줄이지 않고 예측하는 것 시도하기




# Done_List

## Ground Truth
 - test 데이터의 mask 이용 (168개의 이미지)
 - mask 데이터 : 이미지의 픽셀값, 좌표 제공
 - mask의 픽셀값을 이용해서 gt location을 구함 (get_gt.py 코드)

## frcnn을 이용한 사과 detection -> minneapple 데이터셋을 이용해서 학습한 가중치로 예측함
 - https://github.com/nicolaihaeni/MinneApple 코드 참고
 - https://arxiv.org/abs/1909.06441 논문 참고

## yolov5를 이용한 사과 detection -> coco 데이터셋을 이용해서 학습한 가중치로 예측함
 - https://github.com/ultralytics/yolov5 코드 참고
 - yolo_predict.py 코드
 
## IOU 구하기 (get_recall.py에 포함되어있음)
 
## Thresholds에 따른 Recall의 변화 

## AP 구하기
https://github.com/Cartucho/mAP 코드 참고
getAP > yolov5x-results폴더 -> thresholds별 AP, recall, precision 결과
- getAP > input폴더 

## 이미지에 바운딩박스 그리는 코드
- draw_box.py -> gt좌표 잘 구했는지 확인함. rcnn, yolov5 얼마나 잘찾는지 확인함.




 
