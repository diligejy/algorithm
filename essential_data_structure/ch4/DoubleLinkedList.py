class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__prev = None
        self.__next = None

    # 소멸자 : 객체가 사라지기 전 반드시 호출
    # 삭제 연산 때 삭제되는 걸 확인하고자 작성
    def __del__(self):
        print("data of {} is deleted".format(self.data))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, p):
        self.__prev = p

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next = n


class DoubleLinkedList:
    def __init__(self):
        # 리스트의 맨 처음과 마지막은 실제 데이터를 저장하지 않는 노드
        # 이를 더미노드라고 함
        self.head = Node()
        self.tail = Node()

        # 초기화
        # head와 tail을 연결
        self.head.next = self.tail
        self.tail.prev = self.head

        # 데이터 개수를 저장
        self.d_size = 0

    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    def add_first(self, data):
        # 새로운 노드 생성
        new_node = Node(data)
        # next는 더미 노드의 다음 노드, 즉 첫 번째 노드를 가리키도록
        new_node.next = self.head.next
        # prev는 리스트 맨 앞 더미를 가리키도록
        new_node.prev = self.head

        # 첫 번째 데이터 노드의 prev가 새로운 노드를 가리키도록 하고
        self.head.next.prev = new_node
        # 더미 노드의 next는 새로운 노드를 가리켜 새로운 노드 삽입
        self.head.next = new_node

        self.d_size += 1

    def add_last(self, data):
        """
        data를 리스트의 맨 마지막에 추가
        """
        # 새로운 노드 생성
        new_node = Node(data)
        # new node관점에서 왼쪽(tail.prev) 오른쪽(tail) 연결
        new_node.prev = self.tail.prev
        new_node.next = self.tail

        # 기존 tail과 tail.prev관점에서 연결시켜주기
        self.tail.prev.next = new_node
        self.tail.prev = new_node

        self.d_size -= 1

    def insert_after(self, data, node):
        """
        data를 node 다음에 삽입
        node data node.next
        """
        new_node = Node(data)
        new_node.next = node.next
        new_node.prev = node

        node.next.prev = new_node
        node.next = new_node

        self.d_size += 1

    def insert_before(self, data, node):
        """
        data를 node 이전에 삽입
        node.prev data node
        """
        new_node = Node(data)
        new_node.prev = node.prev
        new_node.next = node

        node.prev.next = data
        node.prev = data

        self.d_size += 1

    def search_forward(self, target):
        """
        target을 맨 처음부터 찾아 나가다 리스트에 있으면 노드 반환, 그렇지 않으면 None 반환
        """
        # 데이터 노드를 순회할 cur변수
        cur = self.head.next

        # 리스트의 마지막 노드가 더미 노드 이므로 더미노드가 아니라면 아직 데이터 노드
        while cur is not self.tail:
            if cur.data == target:
                return cur
            cur = cur.next
        return None

    def delete_first(self):
        """
        self.head self.head.next self.head.next.next
        """
        if self.empty():
            return
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

        self.d_size -= 1

    def delete_last(self):
        """
        self.tail.prev.prev self.tail.prev self.tail
        """
        if self.empty():
            return
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

        self.d_size -= 1

    def delete_node(self, node):
        """
        node.prev node node.next
        """
        node.prev.next = node.next
        node.next.prev = node.prev

        self.d_size -= 1


def show_list(dlist):
    print("data size : {}".format(dlist.size()))
    cur = dlist.head.next
    while cur is not dlist.tail:
        print(cur.data, end="  ")
        cur = cur.next
    print()


if __name__ == "__main__":
    dlist = DoubleLinkedList()
    print("*" * 100)
    print("데이터 삽입 -add_first")
    # dlist.add_first(1)
    # dlist.add_first(2)
    # dlist.add_first(3)
    # dlist.add_first(5)

    print("데이터 삽입 -add_last")
    dlist.add_last(1)
    dlist.add_last(2)
    dlist.add_last(3)
    dlist.add_last(5)
    show_list(dlist)

    print("데이터 삽입 - insert_after")
    dlist.insert_after(4, dlist.search_forward(3))
    show_list(dlist)

    print("데이터 삽입 - insert_before")
    dlist.insert_before(4, dlist.search_forward(5))
    show_list(dlist)

    print("데이터 탐색")
    target = 3
    # res=dlist.search_forward(target)
    res = dlist.search_backward(target)
    if res:
        print("데이터 {} 탐색 성공".format(res.data))
    else:
        print("데이터 {} 탐색 실패".format(target))
    res = None

    # print('데이터 삭제-delete_first')
    # dlist.delete_first()
    # dlist.delete_first()

    # print('데이터 삭제-delete_last')
    # dlist.delete_last()
    # dlist.delete_last()

    print("데이터 삭제-delete_node")
    dlist.delete_node(dlist.search_backward(5))

    show_list(dlist)

    print("*" * 100)
