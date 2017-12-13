# https://www.acmicpc.net/problem/10845

class Queue :
    items = []

    def push(self, x) :
        self.items.append(x)

    def pop(self) :
        return -1 if self.empty() == 1 else self.items.pop(0)

    def size(self) :
        return len(self.items)

    def empty(self) :
        return 1 if len(self.items) == 0 else 0

    def front(self) :
        return -1 if self.empty() == 1 else self.items[0]

    def back(self) :
        return -1 if self.empty() == 1 else self.items[len(self.items)-1]

import sys

N = int(input())

read = sys.stdin.readline
write = sys.stdout.write

queue = Queue()

for i in range(N) :
    order = read().split()

    if order[0] == "push"    : queue.push(int(order[1]))
    elif order[0] == "pop"   : write(str(queue.pop()) + "\n")
    elif order[0] == "empty" : write(str(queue.empty()) + "\n")
    elif order[0] == "size"  : write(str(queue.size()) + "\n")
    elif order[0] == "front" : write(str(queue.front()) + "\n")
    elif order[0] == "back"  : write(str(queue.back()) + "\n")


