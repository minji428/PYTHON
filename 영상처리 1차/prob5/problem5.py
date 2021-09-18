"""
6. (고급) unsharp Masking을 블러링하고 감산하는 작업을 없이 단 1회의 공간 필터링으로 수행하는 방안에 대해 검토하시오.
이를 만족하는 커널을 설계하고 그 결과를 원래의 처리 기법과 비교하시오.
"""

import numpy as np, cv2 as cv, matplotlib.pyplot as plt
import os
import cv2
from skimage.util import random_noise


Path = 'data/'
#Name = 'bone(m).bmp'
Name = 'lenna.tif'
#Name = 'monarch.png'
#Name = 'fruits.jpg'
#Name = 'BAR.bmp'

FullName = Path + Name
imgOrg = cv.imread(FullName, 0)
assert imgOrg is not None, "Failed to load image file.."

