# https://www.acmicpc.net/problem/10828
    
class Stack :
    items = []

    def push(self, x) :
        self.items.append(x)

    def pop(self) :
        return -1 if self.empty() == 1 else self.items.pop()

    def size(self) :
        return len(self.items)

    def empty(self) :
        return 1 if len(self.items) == 0 else 0

    def top(self) :
        return -1 if self.empty() == 1 else self.items[len(self.items)-1]
import sys

N = int(input())
stack = Stack()

read = sys.stdin.readline
write = sys.stdout.write

for i in range(N) :
    order = read().split()

    if order[0] == "push"    : stack.push(int(order[1]))
    elif order[0] == "pop"   : write(str(stack.pop()) + "\n")
    elif order[0] == "empty" : write(str(stack.empty()) + "\n")
    elif order[0] == "size"  : write(str(stack.size()) + "\n")
    elif order[0] == "top"   : write(str(stack.top()) + "\n")


