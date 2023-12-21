from __future__ import annotations

from typing import Optional, Callable, Any


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None

    @staticmethod
    def insert(node: Node, value: Optional[int]) -> None:
        if node.value is None:
            node.value = value
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                node.insert(node.left, value)
        elif value >= node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                node.insert(node.right, value)

    @staticmethod
    def search(node: Node, value: Optional[int]) -> Any:
        if node is None or node == value:
            return node
        if value < node.value:
            return node.search(node.left, value)
        else:
            return node.search(node.right, value)

    @staticmethod
    def get_min(node: Node) -> Any:
        if node is None:
            return None
        if node.left is None:
            return node
        return node.get_min(node.left)

    @staticmethod
    def get_max(node: Node) -> Any:
        if node is None:
            return None
        if node.right is None:
            return node
        return node.get_max(node.right)

    def delete(self, node: Node, value: Optional[int]) -> Optional[Node]:
        if node is None:
            return None
        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.value = self.get_min_value(node.right)
            node.right = self.delete(node.right, node.value)
        return node

    def get_min_value(self, node: Node) -> Optional[int]:
        while node.left is not None:
            node = node.left
        return node.value

    @staticmethod
    def in_order_traversal(node: Node) -> Any:  # центровой
        if node is None:
            return None
        node.in_order_traversal(node.left)
        print(node.value, end=" ")
        node.in_order_traversal(node.right)

    @staticmethod
    def preorder_traversal(node: Node) -> Any:  # прямой
        if node is None:
            return None
        print(node.value, end=" ")
        node.preorder_traversal(node.left)
        node.preorder_traversal(node.right)

    @staticmethod
    def postorder_traversal(node: Node) -> Any:  # обратный
        if node is None:
            return None
        node.postorder_traversal(node.left)
        node.postorder_traversal(node.right)
        print(node.value, end=" ")

    @staticmethod
    def stack_preorder_traversal(node: Node) -> Any:
        stack = LinkedStack()
        while (not (node is None)) or (not stack.is_empty()):
            if not stack.is_empty():
                node = stack.pop()
            while not (node is None):
                print(node.value, end=" ")
                if node.right is not None:
                    stack.push(node.right)
                node = node.left

    def set_with_line(self, line: str) -> None:
        notNumbers = "(), "
        ind = 0
        tempLine = line
        while len(tempLine):
            if tempLine[ind] in notNumbers:
                num = tempLine[:ind]
                if num != "":
                    self.insert(self, int(num))
                tempLine = tempLine[ind + 1:]
                ind = 0
            else:
                ind += 1

    @staticmethod
    def print_with_line(node: Node) -> None:
        if node is None:
            return None
        print(node.value, end="")
        if node.left is not None or node.right is not None:
            print(" (", end="")
        node.print_with_line(node.left)
        if node.left is not None or node.right is not None:
            print(", ", end="")
        node.print_with_line(node.right)
        if node.left is not None or node.right is not None:
            print(")", end="")


class LinkedStack:
    def __init__(self) -> None:
        self.top = None

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, item: Node) -> None:
        new_node = Node(item)
        new_node.right = self.top
        self.top = new_node

    def pop(self) -> Any:
        if self.is_empty():
            raise Exception("Stack is empty")
        item = self.top.value
        self.top = self.top.right
        return item

    def peek(self) -> Any:
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value


print("input a binary tree: ")
newLine = input()

Tree = Node()
Tree.set_with_line(newLine)
while True:
    print("\nWhat do you want to do with tree?")
    print("1) insert")
    print("2) delete")
    print("3) search")
    print("4) print preorder")
    print("5) print inorder")
    print("6) print postorder")
    print("7) print with linear bracket view")
    print("8) print stack preorder")
    print("0) exit")
    event = int(input())
    match event:
        case 1:
            print("input a number to insert")
            num = int(input())
            Node.insert(Tree, num)
        case 2:
            print("input a number to delete")
            num = int(input())
            Node.delete(0, Tree, num)
        case 3:
            print("input a number to search")
            num = int(input())
            temp = Node.search(Tree, num)
            Node.print_with_line(temp)
        case 4:
            Node.preorder_traversal(Tree)
        case 5:
            Node.preorder_traversal(Tree)
        case 6:
            Node.preorder_traversal(Tree)
        case 7:
            Node.print_with_line(Tree)
        case 8:
            Node.preorder_traversal(Tree)
        case 0:
            break

Node.print_with_line(Tree)
