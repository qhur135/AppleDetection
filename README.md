# MinneApple Detection

MinneApple dataset을 이용해서 사과를 감지   
데이터셋 다운로드: https://conservancy.umn.edu/handle/11299/206575

- 원래 test 데이터에 mask 없음 &rarr; train 데이터(670개)만 사용
- 402개의 train 데이터, 134개의 val 데이터, 134개의 test 데이터 사용 ( train:val:test = 6:2:2 ) 


## 사용 모델
1. Faster R-CNN
- resnet50을 파인튜닝한 모델
- 402개의 train 데이터와 134개의 val 데이터로 전이 학습 시킨 후, 134개의 test 데이터로 예측함  


2. YOLOv5 
- 402개의 train 데이터와 134개의 val 데이터로 전이 학습 시킨 후, 134개의 test 데이터로 예측함 
- yolov5l 모델 사용 



## Locations 저장 순서 
- Locations 저장 순서(y,x) [ ymin, xmin, ymax, xmax ] 
  &rarr; yolov5 예측 좌표, rcnn 예측 좌표, gt 좌표 저장되어 있음 




## Done_List

## 1. Ground Truth
 - test 데이터의 mask 이용 (670개의 이미지)
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
- coco ap https://github.com/bes-dev/mean_average_precision

## 5. 이미지에 바운딩박스 그리기 
- draw_box.py 코드 &rarr; gt좌표 잘 구했는지 확인함. rcnn, yolov5 얼마나 잘찾는지 확인함.
- green : ground-truth
- red : frcnn predict
- blue : yolov5 predict


## 6. 모델에 따른 검출 성능 비교 
(이미지 크기 640)

|모델|YOLOv5|Faster R-CNN|
|:---------:|:----------:|:------------:|
|정밀도|87.19%|93.72%|
|재현율|56.97%|47.94%|
|F1-Score|68.91%|63.43%|


## 7. 모델에 따른 AP 비교 
(이미지 크기 640)

|모델|YOLOv5|Faster R-CNN|
|:---------:|:----------:|:-----------:|
|AP@IoU=.50:.05:.95|40.66%|38.90%|
|AP@IoU=.50|82.18%|78.98%|
|AP@IoU=.70|52.01%|48.15%|

## 8. YOLOv5 정밀도 향상 실험

임계치에 따른 검출 성능 비교.    
confidence(신뢰도)가 임계치 이상일 때, 사과라고 판단.

|임계치(confidence)|정밀도(IoU=0.5)|재현율(IoU=0.5)|AP(IoU=0.5)|
|:---------:|:----------:|:-----------:|:-----------:|
|85|100%|50.37%|100%|
|80|99.80%|49.92%|99.57%|
|70|99.20%|49.42%|96.39%|
|60|98.31%|48.70%|91.58%|
|50|97.55%|48.07%|87.55%|
|0(전체)|95.86%|51.50%|87.37%|



