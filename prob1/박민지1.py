import time
import os

s_time = time.time()
mysize = os.path.getsize("박민지1.py")
print("Program Size :", f'{mysize:,}')

def print_num(i):
    node = "천백십"
    
    a = i // 10000
    if a > 1:       # 만약 만의 자리가 존재하면 숫자+'만'이라고 a에 저장
        a = str(a) + "만"
    else:           # 아니면 그냥 숫자 저장
        a =""

    b = i % 10000
    data = ""
    limit = 1000
    c = b
    n = 0
    while n < 4:        # 천,백,십, 1로 잘라내기
        if c // limit != 0:
            if c // limit == 1:
                if n < 3:
                    data += node[n]     # 1이면 숫자를 안붙이고 글자만
            else:
                data += str(c // limit)
                if n < 3:               # 숫자랑 단위 다 붙이기
                                        # 1의 자리는 안함
                    data += node[n]

        c = c % limit
        limit //= 10
        n += 1
    if b % 10 == 1:         # 1의 자리 처리
                            # 1의 자리는 무조건 숫자로 처리
        data += str(b % 10)
    data = a + data


    print(f'{i:,}', end=" ")
    print("(", end=" ")
    print(data, end=" ")
    print(")", end=" ")
    print()


int_list = [12334567891, 20500, 1100007, 900001, 9028, 100, 15, 8, 0]
for i in int_list:
    print_num(i)

# num_lines = xxx print_num()의 작성에 소요된 line의 수

c_time = time.time()
print('time: ', c_time-s_time)