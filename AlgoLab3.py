# 3. Инвертировать бинарное дерево поиска. Инвертировать дерево – значит прекомпоновать его элементы
# таким образом, чтобы узлы справа от материнского узла были больше, а слева-меньше.

import random as rnd

class Binary_Tree:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def __get_tree_height(self, node):
        if node is None:
            return 0
        return max(self.__get_tree_height(node.left), self.__get_tree_height(node.right)) + 1

    def get_height(self):
        if self.root is not None:
            return self.__get_tree_height(self.root)

    def __add_node_rec(self, node, key):
        if node is None:
            return self.Node(key)
        elif key < node.key:
            node.left = self.__add_node_rec(node.left, key)
        else:
            node.right = self.__add_node_rec(node.right, key)
        return node

    def add_node(self, key):
        self.root = self.__add_node_rec(self.root, key)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key)
            self.inorder(node.right)

    def print_tree_as_tree(self, node, indent="", last='updown'):
        if node is not None:
            print(indent, end='')

            if last == 'updown':
                print("Root-->", end='')
                indent += "       "
            elif last == 'right':
                print("R--->", end='')
                indent += "|      "
            elif last == 'left':
                print("L--->", end='')
                indent += "       "

            print(node.key)

            self.print_tree_as_tree(node.right, indent, 'right')
            self.print_tree_as_tree(node.left, indent, 'left')

    def __search_key_rec(self, node, key):
        if node is None or node.key == key:
            return node
        elif key < node.key:
            return self.__search_key_rec(node.left, key)
        else:
            return self.__search_key_rec(node.right, key)

    def tree_minimum(self, node):
        if node.left is not None:
            return self.tree_minimum(node.left)
        else:
            return node

    def __delete_node_rec(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self.__delete_node_rec(node.left, key)

        elif key > node.key:
            node.right = self.__delete_node_rec(node.right, key)

        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.tree_minimum(node.right)
            node.key = temp.key
            node.right = self.__delete_node_rec(node.right, temp.key)

        return node

    def __invert_tree_rec(self, node):
        if node is None:
            return None

        node.right, node.left = node.left, node.right

        self.__invert_tree_rec(node.left)
        self.__invert_tree_rec(node.right)

        return node

    def invert_tree(self):
        self.root = self.__invert_tree_rec(self.root)


drzewo = Binary_Tree()
for i in range(8):
    drzewo.add_node(rnd.randint(1,10)*10)

print(f"Высота дерева, нод: {drzewo.get_height()}")
drzewo.print_tree_as_tree(drzewo.root)
drzewo.invert_tree()
drzewo.print_tree_as_tree(drzewo.root)