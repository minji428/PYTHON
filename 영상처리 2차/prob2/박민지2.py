import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

img = cv.imread('data/lenna.tif')
img_array = np.asarray(img)


# 가우시안 2차   (커널사이즈 21, 시그마 3)
kernel1d = cv.getGaussianKernel(21,3)
kernel2d = np.outer(kernel1d,kernel1d.transpose())
#print(kernel2d)

low_img_array = cv.filter2D(img_array, -1, kernel2d)

# 가우시안 2차 한 이미지
low_img = np.array(low_img_array)
cv.imshow('low_img', low_img)

# 푸리에 변환
f = np.fft.fft2(low_img)
fshift = np.fft.fftshift(f)

# 작은 마스크를 만들어 푸리에 변환 영역의 가운데를 지우기
rows, cols,ss = low_img.shape
crow, ccol = rows//2, cols//2
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
f_ishift = np.fft.ifftshift(fshift)
magnitude_spectrum = 20*np.log(np.abs(fshift))

# 다시 이미지 역변환
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(131)
plt.imshow(low_img, cmap='gray')
plt.title('Input Image')

plt.subplot(132)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum')

plt.subplot(133)
plt.imshow(img_back, cmap='gray')
plt.title('Image After')


plt.show()

#sigma = 2; Ksize = floor(sigma * 6) +1; h = fspecial('log', Ksize, sigma)

cv.waitKey()