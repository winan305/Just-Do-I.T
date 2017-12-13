# https://www.acmicpc.net/problem/1991

class Node :
    def __init__(self, data = None, left = None, right = None) :
        self.data = data
        self.left = left
        self.right = right

    def get_data(self) :
        return self.data

    def get_left(self) :
        return self.left

    def get_right(self) :
        return self.right

    def set_data(self, data) :
        self.data = data

    def set_right(self, right) :
        self.right = right

    def set_left(self, left) :
        self.left = left

class BinaryTree :
    def __init__(self) :
        self.root = None

    def get_root(self) :
        return self.root

    def print_tree(self, node) :
        if node != None :
            print("root : ", node.get_data(), end=' ')
            if node.get_left() != None :
                print("left : ", (node.get_left()).get_data(), end=' ')
            if node.get_right() != None :
                print("right : ", (node.get_right()).get_data(), end=' ')

            print()
            self.print_tree(node = node.get_left())
            self.print_tree(node = node.get_right())

    def insert(self, node) :
        if self.root == None :
            self.root = node
        else :
            self.__insert(parent = self.root, node = node)

    def __insert(self, parent, node) :
        if parent == None : return

        if parent.get_data() == node.get_data() :
            parent.set_left(node.get_left())
            parent.set_right(node.get_right())

        else :
            self.__insert(parent.get_left(), node)
            self.__insert(parent.get_right(), node)

    def preorder(self, node) :
        if node == None :
            return

        print(node.get_data(), end='')
        self.preorder(node.get_left())
        self.preorder(node.get_right())

    def inorder(self, node) :
        if node == None :
            return

        self.inorder(node.get_left())
        print(node.get_data(), end='')
        self.inorder(node.get_right())

    def postorder(self, node) :
        if node == None :
            return

        self.postorder(node.get_left())
        self.postorder(node.get_right())
        print(node.get_data(), end='')

import sys

binaryTree = BinaryTree()
N = int(input())

for n in range(N) :
    order = sys.stdin.readline().split()

    parent_node = Node(data = order[0])

    if order[1] != '.' :
        left_child_node = Node(data=order[1])
        parent_node.set_left(left_child_node)

    if order[2] != '.' :
        right_child_node = Node(data=order[2])
        parent_node.set_right(right_child_node)

    binaryTree.insert(node = parent_node)

binaryTree.preorder(node = binaryTree.get_root())
print()
binaryTree.inorder(node = binaryTree.get_root())
print()
binaryTree.postorder(node = binaryTree.get_root())