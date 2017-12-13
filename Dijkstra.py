# https://www.acmicpc.net/problem/1753

import sys
import queue
myInput = sys.stdin.readline
myOutput = sys.stdout.write

# 무한대는 100으로 지정
INFINITY = 100

V, E = map(int, myInput().split())
K = int(myInput())

# 리스트들 생성
nodes = [[] for _ in range(V+1)]
# distance[v] 는 시작점에서 v까지의 거리를 의미한다.
distance = [INFINITY] * (V+1)
distance[K] = 0 # 시작점에서 시작점까지의 거리는 0이다.

# [순위, 아이템] 형식의 튜플로 입력, 숫자가 작을수록 우선순위가 높다.
priority_queue = queue.PriorityQueue()

# u에서 v로 가는 노드의 가중치 저장
for e in range(E) :
    u, v, w = map(int, myInput().split())
    nodes[u].append([v, w])

# 시작점을 우선순위 큐에 삽입
priority_queue.put([distance[K], K])

# 최단경로 계산
# 우선순위 큐가 비지 않을 때 까지 실행한다.
while not priority_queue.empty() :
    # 우선순위큐에서 우선순위가 가장 높은 간선의 거리와 시작점을 가져온다.
    dist, u = priority_queue.get()

    # 그 간선으로부터 이어진 정점까지의 거리를 갱신하고 우선순위 큐에 삽입한다.
    for node in nodes[u] :
        v = node[0]
        weight = node[1]
        if distance[v] > dist + weight :
            distance[v] = dist + weight
            priority_queue.put([distance[v], v])

# 답 출력
for i in range(1, V+1) :
    if distance[i] == INFINITY :
        myOutput("INF\n")
    else :
        myOutput(str(distance[i]) +"\n")


print ("Hello World!")

