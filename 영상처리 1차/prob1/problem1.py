"""
1. 그림 7.1.5의 그림을 출력하는 프로그램.
- 4번째 그림은 m=0.7로 바꿀 것.
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import sys

eps = sys.float_info.epsilon
mid=0;weight=0;E=0

def sigmoid_tablex(m=mid, w=weight, e=E):
    #print(m, w, e)
    r = np.arange(0, 256) / 255.0
    s = (w / (1 + (m/(r+eps))**e)) + (1-weight) * r
    return (255*r).astype(np.uint8)/255

def sigmoid_tabley(m = mid, w = weight, e = E):
    #print(m, w, e)
    r = np.arange(0, 256) / 255.0
    s = (w / (1 + (m/(r+eps))**e)) + (1-weight) * r
    return (255*s).astype(np.uint8)/255


plt.figure(num='Sigmoid Function')      # 창 이름 Sigmoid Function


pltnum = 221    # subplot 위치 정하기

mid = [0.5, 0.5, 0.6, 0.7]
slope = [8, 20, 8, 20]

for i in range(4):
    plt.subplot(pltnum)
    for weight in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
        tablex = sigmoid_tablex(m=mid[i], w=weight, e=slope[i])
        tabley = sigmoid_tabley(m=mid[i], w=weight, e=slope[i])
        plt.plot(tablex, tabley, label=f'w={weight}')
    plt.legend(fontsize=10)  # 네모난 박스 안에 넣을 w 크기

    plt.title(f'Sigmoid Function: m={mid[i]}, E={slope[i]}')
    plt.grid(color='b', linestyle='--', linewidth=0.5)

    plt.xlabel('input: r')  # x 축에 input: r 작성
    plt.ylabel('output: S(r)')  # y 축에 output: S(r) 작성
    pltnum += 1


plt.show()
exit(0)
