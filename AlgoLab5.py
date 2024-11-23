# Написать класс, реализующий структуру данных на базе красно-черного дерева для хранения пар “ключ-значение”

from AlgoLab4 import Czerwono_Czarne_Drewno

class RBDictionary:
    def __init__(self):
        self.tree = Czerwono_Czarne_Drewno()

    def insert(self, key, value):
        """Inserts a key-value pair into the dictionary."""
        self.tree.RB_insert(key, value)

    def get(self, key):
        """Retrieves the value associated with the key."""
        node = self.tree.search_key(key)
        if node:
            return node.value
        return None  # Key not found

    def delete(self, key):
        """Deletes a key-value pair by key."""
        node = self.tree.search_key(key)
        if node:
            self.tree.RB_delete(key)
rb_dict = RBDictionary()


rb_dict.insert("apple", 1)
rb_dict.insert("banana", 2)


print(rb_dict.get("apple"))
print(rb_dict.get("banana"))

rb_dict.delete("apple")
print(rb_dict.get("apple"))