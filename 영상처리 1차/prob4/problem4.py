"""
4. E6.UnsharpMasking.py의 미션
시그마와 고주파 강화용 스케일을 조정하는 2개의 트랙바를 설치하여 이들을 조정하는 Unsharp Masking 프로그램을 설계하시오.
조건: 불필요한 그리기 작업을 무한정 수행하지 않고 트랙바 변동이 있을 때만 화면을 refresh 해야 함.
"""


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

Path = 'data/'

#Name = 'bone(m).bmp'
#Name = 'lenna.tif'
#Name = 'monarch.png'
#Name = 'fruits.jpg'
#Name = 'Fig0303(a)(breast).tif'
#Name = 'tank.bmp'
Name = 'HazyTown.jpg'

FullName = Path + Name
img = cv.imread(FullName)

assert img is not None, "Failed to load image file.."

img = img/255

#b, g, r = cv.split(img); img = cv.merge([r, g, b]);

# blur에서 sigmaX값을 변경해야 고주파 영상을 만들 수 있음
# blur = cv.GaussianBlur(src=img, ksize=(21,21), sigmaX=3,borderType=cv.BORDER_REPLICATE)
# UnsharpMaskImg = img - blur     # 고주파 영상


sigma = 13
scale = 5

# 트랙바 설정
def callBack_sigma(s):
    global scale, sigma
    sigma = s
    #print(sigma)
    #print(scale)

    k = sigma * 6 + 1
    um = img + scale * (img - cv.GaussianBlur(src=img, ksize=(k, k), sigmaX=sigma))
    cv.imshow('UnsharpMasking', um)

def callBack_strength(s):
    global sigma, scale
    scale = s
    #print(sigma)
    #print(scale)

    k = sigma * 6 + 1
    um = img + scale * (img - cv.GaussianBlur(src=img, ksize=(k, k), sigmaX=sigma))
    cv.imshow('UnsharpMasking', um)

cv.namedWindow('UnsharpMasking')
cv.createTrackbar('sigma','UnsharpMasking', 13, 50, callBack_sigma)
cv.createTrackbar('strength','UnsharpMasking', 5, 50,callBack_strength)


while(1):
    k = cv.waitKey(1)
    if k != -1:   # 키를 입력하지 않으면 -1을 반환
        break

