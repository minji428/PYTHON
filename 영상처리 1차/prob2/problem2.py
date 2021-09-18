"""
2. page 21. imadjust(입력영상, 입력범위_리스트,  출력범위_리스트, 감마)  구현
   신규 조건
	입력 영상은 uint8, float(0~1) 제한없어야 함,
	입력영상은 1채널, 3채널 제한 없어야 함.
   	출력 영상은 입력 영상과 같은 데이터형이어야 함.
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image


Path = 'data/'
Name = 'lenna.tif'
#Name = 'bone(m).bmp'
#Name = 'Fig0303(a)(breast).tif'
#Name = 'Fig0306(a)(bone-scan-GE).tif'
#Name = 'CarHeadLightGlare.jpg'
#Name = 'over_exposure.jpg'          # 고조도
#Name = 'tiffany.bmp'                # 고조도
#Name = 'bukak.jpg'                 # 저조도
#Name = 'bk_gate.jpg'
#Name = 'bk_lobby.jpg'

#FullName = Path + Name
FullName ='C:/Users/alswl/OneDrive/바탕 화면/2020년 2학기 수업자료/영상처리 1차 과제/영상처리 1차 과제/prob2/data/lenna.tif'
img = cv.imread(FullName)
assert img is not None, 'No image file....!'

def imadjust(src, input_range=None, output_range=None, gamma=1):
    if input_range is None:
        input_range = (0,1)
    low_in, high_in = input_range
    if output_range is None:
        output_range = (0,1)
    low_out, high_out = output_range

    dst = (((src-low_in)/(high_in-low_in))**gamma)*(high_out-low_out)+low_out

    return dst


img = img/255
dst = imadjust(img,[0.4, 0.7], [0, 1], gamma=1)
cv.imshow('orignal',img)
cv.imshow('streching',dst)
psnr=cv.PSNR(img, dst)
print(round(psnr,4))
cv.waitKey()

org=cv.imread(FullName)/255
img2=imadjust(org,[0, 1], [0.4, 0.7], 0.3)
cv.imshow('mse',img2)
mse=np.sum((org-img2)**2)
#print(mse)

eps = np.finfo(mse).eps
#print(eps)
print(format(mse,"1.3e"))

cv.waitKey()