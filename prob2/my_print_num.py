def print_num(i):
    node = "천백십"
    a = i // 10000

    if a > 1:
        a = str(a) + "만"
    else:
        a =""

    b = i % 10000
    data = ""
    n = 0
    limit = 1000
    c = b
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
        data += str(b % 10)
    data = a + data

    print(f'{i:,}', end=" ")
    print("(", end=" ")
    print(data, end=" ")
    print(")", end=" ")
    print()