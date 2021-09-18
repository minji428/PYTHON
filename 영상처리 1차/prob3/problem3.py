"""
3. Eh5.HistogramSpecification.py 소스의 맨 마지막 줄 미션
미션: 새 창을 열고 src/template/output 영상의 RGB별 히스토그램을 그려 보자.
조건: rgb 히스토그램 데이터를 반환하는 다음 함수를 제작한 후 코딩할 것
r, g, b = myHist(img)
img는 3채널 영상. 부동소수와 uint8을 구분하지 않고 모두 지원할 것
r, g, b는 각각 최댓값에 의해 정규화된 0~1의 분포도.
"""

from skimage.exposure import cumulative_distribution
from skimage.exposure.histogram_matching import _match_cumulative_cdf
from skimage.io import imread
from skimage import exposure
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import sys

path = 'data/'
s_file = 'monarch.png'; t_file = 'forest-park-trail.jpg'

def MyHist(image, reference, multichannel=False):
    if multichannel:
        matched = np.empty(image.shape, dtype=image.dtype)
        for channel in range(image.shape[-1]):
            matched_channel = _match_cumulative_cdf(image[..., channel],
                                                    reference[..., channel])
            matched[..., channel] = matched_channel
    else:
        matched = _match_cumulative_cdf(image, reference)

    return matched

def ncdf(im):
    cdf, b = cumulative_distribution(im)
    for i in range(b[0]):
        cdf = np.insert(cdf, 0, 0)
    for i in range(b[-1]+1, 256):
        cdf = np.append(cdf, 1)
    return cdf

im = imread(path + s_file)      # 원본 영상
im_t = imread(path + t_file)    # template 영상

im1 = MyHist(im, im_t, multichannel=True)


plt.subplot(221), plt.imshow(im1[...,:3]), plt.axis('off'), plt.title('Output Image')   # 첫번째에 결과 이미지 출력

clr_title = ['Red', 'Green', 'Blue']

for i in range(3):          # RGB 채널에 대해 loop 작업
    c = ncdf(im[..., i])     # 원본의 cdf
    c_t = ncdf(im_t[..., i]) # template의 cdf
    c_r = ncdf(im1[...,i])   # 결과의 cdf

    plt.subplot(222+i)

    plt.plot(c * 255, 'r', label='original(ncdf)')
    plt.plot(c_t * 255, 'g', label='template(ncdf)')
    plt.plot(c_r * 255, '--b', label='result(ncdf)')
    plt.title(clr_title[i])
    plt.grid('on'), plt.legend()


plt.savefig('./result.png')     # 영상 저장

plt.show()
exit(0)
