import cv2
import cv2 as cv
import numpy as np, random
from matplotlib.pyplot import box

Path = 'data/'
Name = 'KakaoTalk_20201118_223449005.jpg'
# Name = 'test.png'
Name2 = '3956278e5c1e79e.jpg'
FullName = Path + Name
FullName2 = Path + Name2

ch_key = cv.imread('data/KakaoTalk_20201118_223449005.jpg')
back_gr = cv.imread('data/3956278e5c1e79e.jpg')
# back_gr = cv.imread(FullName2)
assert ch_key is not None, 'No image file....!'
assert back_gr is not None, 'No image file....!'

hsv = 0
lower_blue1 = 0
upper_blue1 = 0
lower_blue2 = 0
upper_blue2 = 0
lower_blue3 = 0
upper_blue3 = 0
img1 = back_gr


def nothing(x):
    pass


def mouse_callback(event, x, y, flags, param):
    global lower_blue1, upper_blue1, lower_blue2, upper_blue2, lower_blue3, upper_blue3, hsv, h_val, s_val, v_val
    if event == cv.EVENT_LBUTTONDOWN:
        print("x,y : ", x, y)  # 마우스 클릭한 부분의 x,y좌표 출력
        color = ch_key[y, x]

        one_pixel = np.uint8([[color]])  # 한픽셀로 구성된 이미지로 변환
        hsv = cv.cvtColor(one_pixel, cv.COLOR_BGR2HSV)  # HSV색 공간으로 변환
        hsv = hsv[0][0]  # HSV 가져오기 위해 픽셀값을 가져옴

        print("bgr : ", color)
        print("hsv : ", hsv)

        h_val = cv.getTrackbarPos('H', 'HSV')
        s_val = cv.getTrackbarPos('S', 'HSV')
        v_val = cv.getTrackbarPos('V', 'HSV')

        #print("h_val : ", h_val)
        #print("s_val : ", s_val)
        #print("v_val : ", v_val)

        # 마우스 클릭한 픽셀값과 유사한 픽셀값 범위 지정
        if hsv[0] < 10:
            lower_blue1 = np.array([hsv[0] - 10 + 180, s_val, v_val])
            upper_blue1 = np.array([180, 255, 255])
            lower_blue2 = np.array([0, s_val, v_val])
            upper_blue2 = np.array([hsv[0], 255, 255])
            lower_blue3 = np.array([hsv[0], s_val, v_val])
            upper_blue3 = np.array([hsv[0] + 10, 255, 255])

        elif hsv[0] > 170:
            lower_blue1 = np.array([hsv[0], s_val, v_val])
            upper_blue1 = np.array([180, 255, 255])
            lower_blue2 = np.array([0, s_val, v_val])
            upper_blue2 = np.array([hsv[0] + 10 - 180, 255, 255])
            lower_blue3 = np.array([hsv[0] - 10, s_val, v_val])
            upper_blue3 = np.array([hsv[0], 255, 255])

        else:
            lower_blue1 = np.array([hsv[0], s_val, v_val])
            upper_blue1 = np.array([hsv[0] + 10, 255, 255])
            lower_blue2 = np.array([hsv[0] - 10, s_val, v_val])
            upper_blue2 = np.array([hsv[0], 255, 255])
            lower_blue3 = np.array([hsv[0] - 10, s_val, v_val])
            upper_blue3 = np.array([hsv[0], 255, 255])


def mouse_callback2(event, x, y, flags, param):
    global image_to_show, s_x, s_y, e_x, e_y, mouse_pressed, drawing_needed

    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스 왼쪽버튼 클릭
        mouse_pressed = True
        s_x, s_y = x, y  # 선택 시작 좌표 기록

    elif event == cv2.EVENT_LBUTTONUP:  # 마우스 왼쪽버튼 떼기
        mouse_pressed = False
        e_x, e_y = x, y  # 선택 종료 좌표 기록
        drawing_needed = True


def bitOperation(hpos, vpos):
    global img1
    img2 = cv.imread('crop.jpg')
    if img1.shape < img2.shape:
        img1 = cv.resize(img1, (1400, 750), interpolation=cv.INTER_AREA)
    # 크롭 이미지 크기 구하기
    rows, cols, channels = img2.shape

    # 이미지 위치 영역 잡기
    roi = img1[vpos:rows + vpos, hpos:cols + hpos]

    # 크롭이미지 흑백 변환 후 마스크 생성
    img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
    mask_inv = cv.bitwise_not(mask)

    img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
    img2_fg = cv.bitwise_and(img2, img2, mask=mask)

    # 검정색 픽셀값은 0이니 검은색은 없어지고 검정색이 아닌 색 출력
    dst = cv.add(img1_bg, img2_fg)
    # 최종 이미지 출력
    img1[vpos:rows + vpos, hpos:cols + hpos] = dst

    cv.imshow('result', img1)

# bgr로 된 이미지파일을 hsv로 변환
img_hsv = cv.cvtColor(ch_key, cv.COLOR_BGR2HSV)
result = img_hsv.copy()
image_to_show = np.copy(result)
mouse_pressed = False
drawing_needed = False
s_x = s_y = e_x = e_y = -1

is_r = False;
is_g = False;
is_b = False
r = [0, 60, 300, 360];
g = [60, 180];
b = [180, 300]
h_val = 10;
s_val = 10;
v_val = 10

cv.namedWindow('A')
cv.setMouseCallback('A', mouse_callback)

cv2.namedWindow('HSV')
cv2.createTrackbar('H', 'HSV', h_val, 360, nothing)
cv2.createTrackbar('S', 'HSV', s_val, 255, nothing)
cv2.createTrackbar('V', 'HSV', v_val, 255, nothing)
cv2.setMouseCallback('HSV', mouse_callback2)
#cv2.setMouseCallback('B', mouse_callback2)

while (1):
    img_color = ch_key

    #height, width = img_color.shape[:2]
    #img_color = cv.resize(img_color, (width, height), interpolation=cv.INTER_AREA)

    k = cv.waitKey(1)

    img_mask1 = cv.inRange(img_hsv, lower_blue1, upper_blue1)
    img_mask2 = cv.inRange(img_hsv, lower_blue2, upper_blue2)
    img_mask3 = cv.inRange(img_hsv, lower_blue3, upper_blue3)
    img_mask = img_mask1 | img_mask2 | img_mask3

    # 마스크 이미지로 원본 이미지에서 범위값에 해당되는 영상 부분 획득
    result = cv.bitwise_and(ch_key, ch_key, mask=img_mask)

    h_val = cv2.getTrackbarPos('H', 'HSV')
    s_val = cv2.getTrackbarPos('S', 'HSV') / 255
    v_val = cv2.getTrackbarPos('V', 'HSV') / 255

    # 이미지 크롭하기
    if drawing_needed == True:
        if s_y > e_y:  # y축상의 시작점과 끝점이 바뀌었으면 두 좌표 바꿈
            s_y, e_y = e_y, s_y
        if s_x > e_x:  # x축상의 시작점과 끝점이 바뀌었으면 두 좌표 바꿈
            s_x, e_x = e_x, s_x

        img_crop = result[s_y:e_y, s_x:e_x]
        cv.imshow('crop', img_crop)
        cv.imwrite('crop.jpg', img_crop)
        drawing_needed = False

    # b버튼을 누르면 배경영상을 출력
    if k == ord('b'):
        cv.imshow('B', back_gr)
        bitOperation(10, 10)


    cv.imshow('A', img_color)
    cv.imshow('HSV', result)

    # c버튼을 누르면 배경에 붙여넣기 한거 취소
    if k == ord('c'):
        pass

    if k == ord('s'):
        cv.imwrite('image.jpg',img1)
    # esc 혹은 q를 누르면 종료
    if k == 27 or k == ord('q'):
        break

cv.destroyAllWindows()
