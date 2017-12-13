# https://www.acmicpc.net/problem/10871

N, X = map(int, input().split())
array = list(map(int, input().split()))

result_list = []
for n in array :
    if n < X : result_list.append(str(n))
print(" ".join(result_list))