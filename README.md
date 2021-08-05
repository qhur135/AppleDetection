# MinneApple Detection

MinneApple dataset을 이용해서 사과를 감지 

- 원래 test 데이터에 mask 없음 &rarr; train 데이터(671개)에서 25% 랜덤으로 뽑아 test 데이터 만듦
- 503개의 train 데이터, 168개의 test 데이터 사용 


## 사용 모델
1. frcnn
- resnet50을 파인튜닝한 모델
- 503개의 train 데이터로 학습 시킨 후, 168개의 test 데이터로 예측함  
- Done_List > 2. frcnn을 이용한 사과 detection 참고 


2. yolov5 
- 168개의 test 데이터로 예측함(minneapple 데이터셋으로 train하지 않음)  
- Done_List > 3. yolov5를 이용한 사과 detection 참고 



## Locations 저장 순서 
- Locations 저장 순서(y,x) [ ymin, xmin, ymax, xmax ] 
  &rarr; yolov5 예측 좌표, rcnn 예측 좌표, gt 좌표 저장되어 있음 


---

## TODO_List
1. apple 아닌 것 빼고 confidence topk 뽑아서 성능 측정
2. k 바꿔가면서 성능 측정
3. 바운딩 박스 유교수님과 맞추기
4. 욜로 다시 학습 - 원래 test 데이터 mask 만들어서 다시 학습시키기 


---


## Done_List

## 1. Ground Truth
 - test 데이터의 mask 이용 (168개의 이미지)
 - mask 데이터 : 이미지의 픽셀값, 좌표 제공
 - mask의 픽셀값을 이용해서 gt location을 구함 (get_gt.py 코드) &rarr; Location > ground-truth 폴더에 저장 


## 2. frcnn을 이용한 사과 detection 
&rarr; minneapple 데이터셋을 이용해서 학습한 가중치로 예측함 
 - https://github.com/nicolaihaeni/MinneApple 코드 참고
 - https://arxiv.org/abs/1909.06441 논문 참고
&rarr; Location > rcnn-results 폴더에 저장


## 3. yolov5를 이용한 사과 detection 
&rarr; coco128 데이터셋을 이용해서 학습한 가중치로 예측함
 - https://github.com/ultralytics/yolov5 코드 참고
 - yolo_predict.py 코드 
 
&rarr; Location > yolov5-results 폴더에 저장 (이미지 크기 640) 

&rarr; Location > yolov5x-1280 이미지 크기를 1280으로 변경 후 예측한 좌표


## 4. AP 구하기 
- yolo_predict.py 실행하면 csv 파일로 좌표 얻을 수 있음 (csv로 저장하는 것이 더 빠르기 때문) 
- 얻은 좌표를 AP_input_format.py에 넣으면 AP 구하는 input format 만들어짐, txt 파일로 저장되도록 함
- getAP > main.py AP 구하는 코드 
- main.py 코드 돌리기 전에 getAP > input 파일 형식 맞추기 &rarr; https://github.com/Cartucho/mAP 참고
- output에 결과 저장


## 5. 이미지에 바운딩박스 그리기 
- draw_box.py 코드 &rarr; gt좌표 잘 구했는지 확인함. rcnn, yolov5 얼마나 잘찾는지 확인함.
- green : ground-truth
- red : frcnn predict
- blue : yolov5 predict


## 6. frcnn AP
thresholds에 따른 AP(이미지 크기 640)
|thresholds(iou)|frcnn(size=640)AP|
|:---------:|:----------:|
|0.0|89.43%|
|0.1|89.16%|
|0.2|89.16%|
|0.3|88.50%|
|0.4|86.80%|
|0.5|83.18%|
|0.6|74.11%|
|0.7|55.32%|
|0.8|23.57%
|0.9|1.10%|
|1.0|0.00%|


## 7. yolov5x 이미지 크기 1280으로 바꾸고 예측하기 
(원래는 이미지 크기 640으로 예측함) 

Thresholds에 따른 AP 
|thresholds(iou)|yolov5x(size=1280)AP|
|:---------:|:----------:|
|0.0|46.34%|
|0.1|46.26%|
|0.2|46.05%|
|0.3|45.25%|
|0.4|43.12%|
|0.5|39.91%|
|0.6|34.98%|
|0.7|26.78%|
|0.8|12.89%
|0.9|0.96%|
|1.0|0.00%|




