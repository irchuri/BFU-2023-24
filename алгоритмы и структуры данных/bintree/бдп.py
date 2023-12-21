from __future__ import annotations
from typing import Any
from random import randint


class Node:
    def __init__(self, key: int = 0) -> None:
        self.key = key
        self.left, self.right = None, None


# корневой узел
root = Node()


def insert_rec(root: Node, key: int) -> Any:
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert_rec(root.left, key)
    else:
        root.right = insert_rec(root.right, key)
    return root


def insert(key: int) -> Any:
    global root
    root = insert_rec(root, key)


def in_order_traversal(root: Node) -> None:
    if root is not None:
        in_order_traversal(root.left)
        print(root.key, end=' ')
        in_order_traversal(root.right)


def tree_insert(arr: list[int]) -> None:
    for item in arr:
        insert(item)


spisok = [randint(-100, 100) for i in range(10)]
tree_insert(spisok)
in_order_traversal(root)
