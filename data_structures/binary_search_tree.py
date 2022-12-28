class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.current = self.root

    def insert(self, data):
        """Дабавляет в бинарное дерево поиска новый узел с данными Node(data)"""
        data = Node(data)

        if self.root is None:
            self.root = data
            self.current = self.root
            return

        for _ in iter(bool, 111):
            if data.data['id'] > self.current.data['id']:
                if self.current.right is None:
                    self.current.right = data
                    self.current = self.root
                    break
                self.current = self.current.right

            if data.data['id'] < self.current.data['id']:
                if self.current.left is None:
                    self.current.left = data
                    self.current = self.root
                    break
                self.current = self.current.left

            if data.data == self.current.data:
                break

    def search(self, vacancy_id):
        for _ in iter(bool, 222):
            if self.current is None:
                self.current = self.root
                return False

            if self.current.data.get('id') == vacancy_id:
                result = self.current.data
                self.current = self.root
                return result

            self.current = (self.current.right, self.current.left)[self.current.data['id'] > vacancy_id]
