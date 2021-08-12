class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
    def __str__(self):
        return str(self.key)


a = Node(3)
b = Node(9)
c = Node(-1)

a.next = b
b.next = c

# 매 노드마다 이름 설정 하지 않고 Head, size로 구성된 빈 리스트를 이용해서 연결
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = self.Head
        self.head = new_node
        self.size += 1
    
    def pushBack(self, key):
        new_node = Node(key)
        if len(self) == 0:
            self.head = new_node
        else:
            tail = self.head 
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def popFront(self):
        if len(self) == 0:
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next
            self.size -= 1
            del x
            return key

    def popBack(self):
        if len(self) == 0:
            return None
        else:
            # running technique
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if len(self) == 1:
                self.head = None
            prev.next = tail.next
            key = tail.key
            del tail
            self.size -= 1
            return key