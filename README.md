# MinneApple_Detection
MinneApple dataset을 이용해서 사과를 감지
- frcnn 사용
- test 데이터 기존의 test 데이터 사용하지 않고 train에서 랜덤으로 25% 선택함 (기존의 test 데이터에는 mask가 없기 때문)

Done_List
1. Ground Truth
 - test 데이터의 mask 이용 (168개의 이미지)
 - mask 데이터 : 이미지의 픽셀값, 좌표 제공
 - mask의 픽셀값을 이용해서 gt location을 구함 (get_gt.py 코드)

2. frcnn을 이용한 사과 detection
 - https://github.com/nicolaihaeni/MinneApple 코드 참고
 - https://arxiv.org/abs/1909.06441 논문 참고
 - output.txt로 location 결과 나옴 -> 정제해서 사용




TODO_List
