class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.is_first = False

    def enqueue(self, data):
        """Добавить данные в очередь"""
        if not self.is_first:
            self.head = Node(data)
            self.tail = self.head
            self.is_first = True
            return
        it = Node(data)
        self.tail.next_node = it
        self.tail = it

    def dequeue(self):
        """Забрать данные из очереди"""
        if not self.is_first:
            return
        self.head = self.head.next_node

    def to_list(self):
        """Вернуть данные очереди в виде списка"""
        result = []
        if not self.is_first:
            return result
        current = self.head
        while True:
            if current is None:
                break
            if current.data is None:
                current = current.next_node
                continue
            result.append(current.data)
            current = current.next_node
        return result
