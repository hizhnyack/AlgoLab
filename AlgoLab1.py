# Сделать реверс односвзяного списка.
# Пример:
# Входные данные: 1, 2, 3, 4, 5
# Результат: 5, 4, 3, 2, 1


class LinkedList:
    class Node:
        def __init__(self, key):
            self.key = key
            self.next = None

    def __init__(self):
        self.head = None

    def __add_node_rec(self, node, key):
        if node.next:
            self.__add_node_rec(node.next, key)
        else:
            new_node = self.Node(key)
            node.next = new_node

    def add_element(self, key):
        if self.head is None:
            self.head = self.Node(key)
        else:
            self.__add_node_rec(self.head, key)

    def __rev_list_rec(self, prev_node, curr_node):
        if curr_node is None:
            self.head = prev_node
            return

        next_node = curr_node.next
        curr_node.next = prev_node

        self.__rev_list_rec(curr_node, next_node)

    def reverse_list(self):
        if self.head is not None:
            self.__rev_list_rec(None, self.head)

    def list_elements(self):
        tmp = self.head
        while tmp:
            print(tmp.key, "-",end = ' ')
            tmp = tmp.next
        print("End")


list = LinkedList()
for i in range(5):
    list.add_element(i+1)
list.list_elements()
list.reverse_list()
list.list_elements()