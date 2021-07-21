import os
import os.path
import time
import sys
from matplotlib import pyplot as plt
import cv2 as cv
from skimage.io import imread
from my_print_num import *

s_time = time.time()

mysize = os.path.getsize("박민지2.py")
print("Program Size :", f'{mysize:,}')

src_folder = 'mission3_personal_data_removed/'

def allFiles(path):  # 하위 디렉토리에 존재하는 jpg, png, tif 구하기
    test = []
    for current, dir, files in os.walk(path):
        currentpath = os.path.join(os.path.abspath(""), current)
        for file in files:  # 파일 확장자가 다음과 같으면 주소와 파일명 합치기
            if file.endswith('.jpg'):
                filepath = os.path.join(currentpath, file)
                test.append(filepath)
            elif file.endswith('.png'):
                filepath = os.path.join(currentpath, file)
                test.append(filepath)
            elif file.endswith('.tif'):
                filepath = os.path.join(currentpath, file)
                test.append(filepath)
            elif file.endswith('.JPG'):
                filepath = os.path.join(currentpath, file)
                test.append(filepath)
            elif file.endswith('.PNG'):
                filepath = os.path.join(currentpath, file)
                test.append(filepath)
            elif file.endswith('.TIF'):
                filepath = os.path.join(currentpath, file)
                test.append(filepath)
    return test

def getsize(path_dir):  # 영상 크기 구하기
    file_size = os.path.getsize(path_dir)
    return file_size

def getSortData(name):
    jpg = []
    png = []
    tif = []

    for i in name:
        if ".jpg" in i:
            jpg.append(i)
        elif ".png" in i:
            png.append(i)
        elif ".tif" in i:
            tif.append(i)
        elif ".JPG" in i:
            jpg.append(i)
        elif ".PNG" in i:
            png.append(i)
        elif ".TIF" in i:
            tif.append(i)
    return len(jpg), len(png), len(tif)

def Min_Size(name, size):  # 파일사이즈 제일 작은거
    lst1 = []  # 파일명
    lst2 = []  # 파일 사이즈

    for i in name:
        lst1.append(i)
    for i in size:
        lst2.append(i)

    for i in range(len(lst2)):
        for j in range(len(lst2)):
            if lst2[i] < lst2[j]:
                temp = lst2[i]
                lst2[i] = lst2[j]
                lst2[j] = temp

                temp = lst1[i]
                lst1[i] = lst1[j]
                lst1[j] = temp

    return lst1[0], lst2[0]

def Max_Size(name, size):  # 파일 사이즈 제일 큰거
    lst1 = []  # 파일명
    lst2 = []  # 파일 사이즈

    for i in name:
        lst1.append(i)
    for i in size:
        lst2.append(i)

    for i in range(len(lst2)):
        for j in range(len(lst2)):
            if lst2[i] > lst2[j]:
                temp = lst2[i]
                lst2[i] = lst2[j]
                lst2[j] = temp

                temp = lst1[i]
                lst1[i] = lst1[j]
                lst1[j] = temp

    return lst1[0], lst2[0]

def heightSize(name):
    n = []
    hei = []
    wid = []
    channel = []

    for i in name:  # 파일 명을 src_folder로 잘라서 mission 이후의 폴더 이름만 n에 저장
        j = i.split(src_folder)
        k = j[1]
        l = os.path.join(src_folder, k)
        n.append(l)
    for i in range(len(n)):  # 저장된 주소를 불러와서 img에 저장 후 그 이미지의 h,w,c 구함
        img = cv.imread(n[i])
        heig, wide, chan = img.shape
        hei.append(heig)
        wid.append(wide)
        channel.append(chan)

    for i in range(len(n)):
        for j in range(len(n)):
            if hei[i] > hei[j]:
                temp = hei[i]  # 크기 위치 변경
                hei[i] = hei[j]
                hei[j] = temp

                temp = wid[i]
                wid[i] = wid[j]
                wid[j] = temp

                temp = n[i]  # 크기 위치로 이름 변경
                n[i] = n[j]
                n[j] = temp

    return n[0], hei[0], wid[0]

def wideSize(name):
    n = []
    hei = []
    wid = []
    channel = []

    for i in name:  # 파일 명을 src_folder 잘라서 mission 이후의 폴더 이름만 n에 저장
        j = i.split(src_folder)
        k = j[1]
        l = os.path.join(src_folder, k)
        n.append(l)

    for i in range(len(n)):  # 저장된 주소를 불러와서 img에 저장 후 그 이미지의 h,w,c 구함
        img = cv.imread(n[i])
        heig, wide, chan = img.shape
        hei.append(heig)
        wid.append(wide)
        channel.append(chan)

    for i in range(len(n)):
        for j in range(len(n)):
            if wid[i] > wid[j]:
                temp = hei[i]  # 크기 위치 변경
                hei[i] = hei[j]
                hei[j] = temp

                temp = wid[i]
                wid[i] = wid[j]
                wid[j] = temp

                temp = n[i]  # 크기 위치로 이름 변경
                n[i] = n[j]
                n[j] = temp

    return n[0], hei[0], wid[0]

def namesplit(name):
    y = name.split('/')
    y.reverse()
    splitname = y[0]

    return splitname


name1 = allFiles(src_folder)    # 이미지 파일의 디렉토리 주소
name = []
size = []       # 이미지 파일의 크기
for i in name1:
    s = i.replace("\\", "/")
    name.append(s)
    size.append(getsize(i))

jpg, png, tif = getSortData(name)       # 각 확장자 마다 이미지 파일의 개수

MaxName, MaxSize = Max_Size(name, size)
MinName, MinSize = Min_Size(name, size)
heina, heihei, heiwid = heightSize(name)  # 세로가 제일 높은 이미지
widna, widhei, widwid = wideSize(name)     # 가로가 제일 높은 이미지


total = jpg + png + tif     # 이미지 파일의 개수
totalsize = 0   # 이미지 파일의 총 크기
for i in size:
    totalsize += i

print('Total number of picture files : {0}(jpg : {1}, png : {2}, tif : {3})'.format(total, jpg, png, tif))
print('Total size of files : ', end=" "), print_num(totalsize)


# 디렉토리 주소에서 파일명과 확장자명만 출력하기
Maxfilename = namesplit(MaxName)
Minfilename = namesplit(MinName)
widname = namesplit(widna)
heiname = namesplit(heina)


# 영상 출력
img = imread(MaxName)
plt.figure()
plt.subplot(221), plt.imshow(img)
plt.axis('off')
plt.title('max={0} ({1})'.format(Maxfilename, f'{MaxSize:,}'))

img = imread(MinName)
plt.subplot(222), plt.imshow(img)
plt.axis('off')
plt.title('min={0} ({1})'.format(Minfilename, MinSize))

img = imread(heina)
plt.subplot(223), plt.imshow(img)
plt.axis('off')
plt.title('tall={0} ({1},{2})'.format(heiname, heihei, heiwid))

img = imread(widna)
plt.subplot(224), plt.imshow(img)
plt.axis('off')
plt.title('wide={0} ({1},{2})'.format(widname, widhei, widwid))

c_time = time.time()
print('time: ', c_time - s_time)

plt.show()

