# https://www.acmicpc.net/problem/2581

def isPrime(n) :
    if n == 1 : return False
    i = 2
    while i*i <= n :
        if n%i == 0 : return False
        i+=1

    return True

M = int(input())
N = int(input())

primes = []
sum = 0
for n in range(M, N+1) :
    if isPrime(n) :
        sum += n
        primes.append(n)
if sum == 0 : print(-1)
else :
    print(sum)
    print(primes[0])

