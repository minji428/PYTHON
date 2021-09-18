from PIL import Image, ImageDraw, ImageFont
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

orig_img = 'data/lenna.bmp'
res_img = 'data/watermark.bmp'
watermark_img = 'watermark.bmp'


def callBack_bit(b):
    img = cv.imread(watermark_img, cv.IMREAD_GRAYSCALE)

    row, col = img.shape
    result_img = img.copy()

    for i in range(0, row):
        for j in range(0, col):
            result_img[i, j] = 255 if (img[i, j] & (1 << b)) else 0

    cv.imshow('WaterMark', result_img)

def watermark():
    img = cv.imread(orig_img, cv.IMREAD_GRAYSCALE)
    water_img = cv.imread(res_img, cv.IMREAD_GRAYSCALE)

    result_img = img.copy()

    row,col = img.shape

    for i in range(0,row):
        for j in range(0, col):
            if water_img[i,j] == 0:     # 그레이스케일 값이 0인 부분, 검은색 부분
                result_img[i,j] = img[i,j]&254
            else:   # 그레이스케일 값이 0이 아닐 때, 검은색이 아니면 흰색으로 처리
                result_img[i,j] = img[i,j]|1
    cv.imwrite('watermark.bmp',result_img)

cv.namedWindow('WaterMark')
cv.createTrackbar('bit','WaterMark', 0,8, callBack_bit)

while(1):
    watermark()
    k = cv.waitKey(1)
    if k != -1:
        break
