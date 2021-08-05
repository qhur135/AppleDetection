# MinneApple Detection

MinneApple dataset을 이용해서 사과를 감지

- frcnn, yolov5 사용
- test 데이터 기존의 test 데이터 사용하지 않고 train에서 랜덤으로 25% 선택함 (기존의 test 데이터에는 mask가 없기 때문)



## Locations 저장 순서 
- Locations 저장 순서(y,x) [ ymin, xmin, ymax, xmax ] 
  &rarr; yolov5 예측 좌표, rcnn 예측 좌표, gt 좌표 저장되어 있음 


---

## TODO_List
1. apple 아닌 것 빼고 confidence topk 뽑아서 성능 측정
2. k 바꿔가면서 성능 측정
3. 바운딩 박스 유교수님이랑 맞추기
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
&rarr; coco 데이터셋을 이용해서 학습한 가중치로 예측함
 - https://github.com/ultralytics/yolov5 코드 참고
 - yolo_predict.py 코드
&rarr; Location > yolov5-results 폴더에 저장


## 4. AP 구하기 
https://github.com/Cartucho/mAP 코드 참고



## 5. 이미지에 바운딩박스 그리기 
- draw_box.py &rarr; gt좌표 잘 구했는지 확인함. rcnn, yolov5 얼마나 잘찾는지 확인함.
- green : ground-truth
- red : frcnn predict
- blue : yolov5x predict


## 6. yolov5x 이미지 크기 1280으로 바꾸고 예측하기 
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




