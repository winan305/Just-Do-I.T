# https://www.acmicpc.net/problem/2577

abc = 1
count = [0] * 10

for n in range(3) :
    abc *= int(input())

for c in str(abc) :
    count[int(c)]+=1

for i in range(10) :
    print(count[i])