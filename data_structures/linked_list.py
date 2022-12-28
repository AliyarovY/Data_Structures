class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.last_node = self.head

    def to_list(self):
        """Возвращает список, содержащий данные узлов связанного списка"""
        result = []
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

    def print_ll(self):
        """Возвращает строку-представление связанного списка для печати"""
        res = ''
        for j in self.to_list():
            if j is None:
                continue
            res += f'{j} -> '
        res += 'None'
        return res

    def insert_beginning(self, data):
        """Добавить данные в началов связанного списка"""
        new = Node(data, self.head)
        self.head = new

    def insert_at_end(self, data):
        """Добавить данные в конец связанного списка"""
        append_item = Node(data=data)
        self.last_node.next_node = append_item
        self.last_node = append_item

    def get_vacancy_by_id(self, vacancy_id):
        """Получить данные из связанного списка по id"""
        for j in self.to_list():
            if j['id'] == vacancy_id:
                return j
        return None
