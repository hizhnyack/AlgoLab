# Реализовать балансировку красно-черного дерева.


class Czerwono_Czarne_Drewno():
    class Node():
        def __init__(self, key=None):
            self.parent = None
            self.key = key
            self.right = None
            self.left = None
            self.color = True

    def __init__(self, key=None):
        self.root = self.Node(key) if key else None

    def __search_key_rec(self, node, key):
        if node is None or node.key == key:
            return node
        elif key < node.key:
            return self.__search_key_rec(node.left, key)
        else:
            return self.__search_key_rec(node.right, key)

    def search_key(self, key):
        if self.root is not None:
            result = self.__search_key_rec(self.root, key)
            return result

    def print_tree_as_tree(self, node, indent="", last='updown'):
        if node is not None:
            print(indent, end='')

            if last == 'updown':
                print("Root->", end='')
                indent += "       "
            elif last == 'right':
                print("R--->", end='')
                indent += "|      "
            elif last == 'left':
                print("L--->", end='')
                indent += "       "

            print(f"{node.color}")

            self.print_tree_as_tree(node.right, indent, 'right')
            self.print_tree_as_tree(node.left, indent, 'left')

    def left_rotate(self, node):
        y = node.right
        node.right = y.left
        if y.left is not None:
            y.left.parent = node

        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y

        else:
            node.parent.right = y

        y.left = node
        node.parent = y

    def right_rotate(self, node):
        y = node.left

        node.left = y.right

        if y.right is not None:
            y.right.parent = node

        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y

        else:
            node.parent.right = y

        y.right = node
        node.parent = y

    def _get_black_height(self, node):
        if node is None:
            return 1

        left_height = self._get_black_height(node.left)
        right_height = self._get_black_height(node.right)

        if left_height == -1 or right_height == -1 or left_height != right_height:
            return -1

        return left_height + (1 if not node.color else 0)

    def get_black_height(self):
        if self.root is not None:
            return self._get_black_height(self.root)

    def RB_insert(self, val):
        insert_node = self.Node(val)
        temp_node = self.root
        temp_parent = None
        while temp_node is not None:
            temp_parent = temp_node
            if insert_node.key < temp_node.key:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right

        insert_node.parent = temp_parent
        if temp_parent is None:
            self.root = insert_node

        elif insert_node.key < temp_parent.key:
            temp_parent.left = insert_node
        else:
            temp_parent.right = insert_node

        self.RB_insert_fixup(insert_node)

    def RB_insert_fixup(self, node):
        while node != self.root and node.parent.color:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right  # The "uncle" node
                if uncle and uncle.color:  # Case 1: Uncle is red (recoloring)
                    node.parent.color = False
                    uncle.color = False
                    node.parent.parent.color = True
                    node = node.parent.parent
                else:  # Uncle is black, perform rotations
                    if node == node.parent.right:  # Case 2: Node is a right child
                        node = node.parent
                        self.left_rotate(node)
                        # Case 3: Node is a left child (right rotation needed)
                    node.parent.color = False
                    node.parent.parent.color = True
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color:
                    node.parent.color = False
                    uncle.color = False
                    node.parent.parent.color = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = False
                    node.parent.parent.color = True
                    self.left_rotate(node.parent.parent)

        self.root.color = False

    def RB_transplant(self, node1, node2):
        if node1.parent is None:
            self.root = node2
        elif node1 == node1.parent.left:
            node1.parent.left = node2
        else:
            node1.parent.right = node2

        node2.parent = node1.parent

    def RB_delete(self, val):
        node_to_delete = self.search_key(val)
        if node_to_delete is None:
            print(f"Value {val} not found in the tree.")
            return

        # Proceed with the deletion process if the node exists

        original_node = node_to_delete
        original_node = node_to_delete
        original_color = original_node.color
        if node_to_delete.left is None:
            replacement_node = node_to_delete.right
            self.RB_transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right is None:
            replacement_node = node_to_delete.left
            self.RB_transplant(node_to_delete, node_to_delete.left)
        else:
            original_node = self.find_minimum(node_to_delete.right)
            original_color = original_node.color
            replacement_node = original_node.right
            if original_node.parent == node_to_delete:
                replacement_node.parent = original_node
            else:
                self.RB_transplant(original_node, original_node.right)
                original_node.right = node_to_delete.right
                original_node.right.parent = original_node

            self.RB_transplant(node_to_delete, original_node)
            original_node.left = node_to_delete.left
            original_node.left.parent = original_node
            original_node.color = node_to_delete.color

        if original_color == False:
            self.RB_delete_fixup(replacement_node)

    def RB_delete_fixup(self, node):
        while node != self.root and node.color == False:
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color:  # Case 1: Sibling is red
                    sibling.color = False
                    node.parent.color = True
                    self.left_rotate(node.parent)
                    sibling = node.parent.right
                if ((sibling.left.color == False if sibling.left else True) and
                        (
                        sibling.right.color == False if sibling.right else True)):  # Case 2: Both children of sibling are black
                    sibling.color = True
                    node = node.parent
                else:
                    if sibling.right.color == False if sibling.right else True:  # Case 3: Right child of sibling is black
                        sibling.left.color = False
                        sibling.color = True
                        self.right_rotate(sibling)
                        sibling = node.parent.right
                    # Case 4: Right child of sibling is red
                    sibling.color = node.parent.color
                    node.parent.color = False
                    sibling.right.color = False
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color:
                    sibling.color = False
                    node.parent.color = True
                    self.right_rotate(node.parent)
                    sibling = node.parent.left
                if ((sibling.right.color == False if sibling.right else True) and
                        (sibling.left.color == False if sibling.left else True)):
                    sibling.color = True
                    node = node.parent
                else:
                    if sibling.left.color == False if sibling.left else True:
                        sibling.right.color = False
                        sibling.color = True
                        self.left_rotate(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = False
                    sibling.left.color = False
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = False


ccDrewno = Czerwono_Czarne_Drewno()
values = [10, 20, 30, 15, 25, 5, 1]
for val in values:
    ccDrewno.RB_insert(val)

ccDrewno.print_tree_as_tree(ccDrewno.root)
ccDrewno.RB_delete(5)

ccDrewno.print_tree_as_tree(ccDrewno.root)
print(ccDrewno.get_black_height())