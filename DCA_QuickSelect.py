# https://www.acmicpc.net/problem/11004

import sys

myInput = sys.stdin.readline
myOutput = sys.stdout.write


def quick_select(list, k):
    pivot = list[0]
    small_list, big_list = [], []
    # 피벗보다 작은 리스트와 크거나 같은 리스트.
    # 작은 리스트의 끝에 피벗을 추가한다.

    for i in range(1, len(list)):
        # list[0]이 피벗이기 때문에 1부터 반복한다.
        if list[i] < pivot:
            small_list.append(list[i])
        else:
            big_list.append(list[i])

    small_list.append(pivot)
    pivotIndex = len(small_list) - 1
    # 피벗의 위치는 작은 리스트의 마지막 인덱스와 같다.

    list = small_list + big_list
    # 피벗을 기준으로 정렬된 결과 리스트

    if pivotIndex == k - 1:
        return list[pivotIndex]
    elif pivotIndex < k - 1:  # 피벗의 위치보다 큰 위치에 존재
        k = k - len(small_list)  # k의 값을 조정해 주어야 한다.
        return quick_select(big_list, k)
    else:  # 피벗의 위치보다 작은 위치에 존재
        return quick_select(small_list, k)


NK = myInput().split()

N = int(NK[0])
K = int(NK[1])

A = list(map(int, myInput().split()))

myOutput(str(quick_select(A, K)))