# MinneApple_Detection
MinneApple dataset을 이용해서 사과를 감지
- frcnn 사용
- test 데이터 기존의 test 데이터 사용하지 않고 train에서 랜덤으로 25% 선택함 (기존의 test 데이터에는 mask가 없기 때문)
- Locations 저장 순서 [ ymin, xmin, ymax, xmax ]

Done_List
1. Ground Truth
 - test 데이터의 mask 이용 (168개의 이미지)
 - mask 데이터 : 이미지의 픽셀값, 좌표 제공
 - mask의 픽셀값을 이용해서 gt location을 구함 (get_gt.py 코드)

2. frcnn을 이용한 사과 detection
 - https://github.com/nicolaihaeni/MinneApple 코드 참고
 - https://arxiv.org/abs/1909.06441 논문 참고

3. IOU 구하기 (get_recall.py에 포함되어있음)
4. 
5. Thresholds에 따른 Recall의 변화 

TODO_List
1. 논문 읽기 - Recall, Precision 어떻게 구했나 확인
2. Precision 구하기
3. Recall 제대로 구한거 맞는지 확인
4. PR 곡선 그리기
5. AP 그리기
