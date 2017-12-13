# https://www.acmicpc.net/problem/4673

def d(n) :
    generator = n
    while n > 0 :
        generator = generator + (n%10)
        n = n//10
    return generator

isSelf = [True] * 10001 # 10001개의 리스트를 생성하면 0 ~ 10000 까지의 인덱스로 접근가능.

for i in range(1, 10001) :
    generator = d(i)
    if(generator < 10001) : isSelf[generator] = False

for i in range(1, 10001) :
    if(isSelf[i] == True) : print(i)

