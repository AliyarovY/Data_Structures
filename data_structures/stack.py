class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """Добавить элемент в стэк"""
        it = Node(data)
        if self.top is None:
            self.top = it
            return
        it.next_node = self.top
        self.top = it

    def pop(self):
        """Удалить элемент из стека и вернуть значение этого элемента"""
        if self.top is None:
            return
        ret = self.top.data
        if self.top.next_node != None:
            self.top, self.top.next_node = self.top.next_node, None
        else:
            self.top = self.top.next_node
        return ret

    def to_list(self):
        """Вернуть данные стека в виде списка"""
        if self.top is None:
            return []
        res = []
        cr = self.top
        while not cr is None:
            if cr.data is None:
                continue
            res.append(cr.data)
            cr = cr.next_node
        return res


def t():
    s = Stack()
    assert s.to_list() == []

    s = Stack()
    s.push('data1')
    s.push({'key': 'value'})
    s.push(1000)

    assert s.to_list() == [1000, {'key': 'value'}, 'data1']

    s = Stack()
    removed = s.pop()

    assert removed is None

    s = Stack()
    s.push(100)
    removed = s.pop()

    assert removed == 100
    assert s.to_list() == []

    s = Stack()
    s.push(100)
    s.push([5])

    assert s.pop() == [5]
    assert s.pop() == 100
    assert s.pop() is None
    assert s.to_list() == []



