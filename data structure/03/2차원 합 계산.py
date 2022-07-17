import time, random


def sum1(A, n):
    # code here
    B = [
        [0] * n
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(i, n):
            B[i][j] = sum(A[i:j + 1])


# n = 1 이상 5000 이하 정수 값 입력
n = int(input())

# 리스트 A에 랜덤 정수 값 n개 채움
A = [
    random.randint(0, 100)
    for _ in range(n)
]

# sum 함수 호출 + 시간 측정
before = time.process_time()
sum1(A, n)
after = time.process_time()

# 함수의 수행시간을 출력
print(after - before)