import os

# 변수의 위치를 지정하는 변수
path_dir = "C:/Users/alswl/OneDrive/바탕 화면/2021년 1학기 수업자료/자바"

def getDataName(path_dir):          # 폴더 안에 들어있는 파일 명 가져오는 함수
    file_list = os.listdir(path_dir)

    test = []       # 폴더 안에 들어 있는 폴더
    for i in file_list:
        if "." not in i:
            test.append(i)

    return file_list, test

def getDataSize(path_dir):          # 폴더 안에 들어있는 파일의 크기 가져오는 함수
    file_list = os.listdir(path_dir)
    a = []

    for i in file_list:
        b = os.path.getsize(path_dir+"/"+i)
        if b != 0:                  # 만약 폴더 안에 폴더가 있으면 폴더의 크기를 가져오지 않음
            a.append(b)
    return a

def getSort(data, size):        # 확장자명 순으로 sort하는 함수
    lst1 = []       # 확장자
    lst2 = []       # 파일이름
    test = []       # 하나하나의 파일명

    for i in data:
        if "." in i:
            test.append(i)
    data = test

    for i in data:
        test = i.split(".")
        lst1.append(test[1])        # 확장자
        lst2.append(test[0])

    for i in range(len(lst1)):          # 셔플을 사용해서 확장자를 알파벳 순으로 소팅
        for j in range(len(lst1)):
            if lst1[i] < lst1[j]:
                temp = lst1[i]
                lst1[i] = lst1[j]
                lst1[j] = temp

                temp = lst2[i]
                lst2[i] = lst2[j]
                lst2[j] = temp

                temp = size[i]
                size[i] = size[j]
                size[j] = temp

    lst3 = []           # .으로 나눴던 이름과 확자자명 합치기
    for i in range(len(lst1)):
        lst3.append(lst2[i] + "." + lst1[i])

    return lst3,size

def getCount(so):   # 확장자명별로 개수, 크기 세기
    data = so[0]    # 폴더가 아닌 파일 데이터
    size = so[1]    # 사이즈

    test = []
    for i in data:
        if "." in i:
            test.append(i)
    data = test

    kind = []
    count = []
    sizeall = []

    for i in data:
        test = i.split(".")
        if test[1] not in kind:
            kind.append(test[1])
            count.append(0)
            sizeall.append(0)

    k = 0
    for i in data :
        test = i.split(".")
        for n in range(len(kind)):
            if kind[n] == test[1]:
                count[n] += 1
                sizeall[n] += size[k]
        k += 1

    return kind, count, sizeall


fileName = []       # 확장자명
fileCount = []      # 확장자명당 개수
fileSize = []       # 각 확장자명의 크기 합
folderList = []

name,folderList = getDataName(path_dir)
size = getDataSize(path_dir)
so = getSort(name, size)
fileName,fileCount,fileSize = getCount (so)


# 총 파일의 수
ftotal = 0
for i in fileCount:
    ftotal += i

# 총 용량
total = 0
for i in fileSize:
    total += i


# 총 폴더(파일x)의 수
folderNum = len(folderList)



print()
print("파일: ","\t",("개수:").rjust(5),"\t",("파일 크기의 합"),"\t","퍼센트 용량")
for i in range(len(fileName)):
    print(fileName[i].ljust(10), (f'{fileCount[i]:,}').rjust(5),"\t", (f'{fileSize[i]:,}').rjust(12),"\t",str(round(fileSize[i]/total*100,4)).rjust(8),"%")

print()
print("폴더:")
for i in folderList:
    print("<"+i+">")

print()
print("확장자의 수 =",len(fileName),"\t","폴더의 수 =",f'{folderNum:,}',"\t","총 파일의 수 =",f'{ftotal:,}',"\t","총 용량 =",f'{total:,}')
