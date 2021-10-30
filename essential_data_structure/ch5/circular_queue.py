class CQueue:
    # 원형 큐가 잘 작동하는지 확인하려고 동적 배열의 크기를 작게 잡음
    MAXSIZE = 10

    def __init__(self):
        self.container = [None for _ in range(CQueue.MAXSIZE)]
        self.front = 0 
        self.rear = 0

    def is_empty(self):
        if self.front == self.rear:
            return True
        return False
    
    def __step_forward(self, x):
        """
        편의함수 : front나 rear를 뒤로 이동했을 때 동적 배열을 벗어난다면 동적 배열의 맨 처음으로 이동
        """
        x += 1
        if x >= CQueue.MAXSIZE:
            x = 0
        return x

    def is_full(self):
        next = self.__step_forward(self.rear)
        if next == self.front:
            return True
        return False
    
    def enqueue(self, data):
        if self.is_full():
            raise Exception("The queue is full")
        self.container[self.rear] = data
        self.rear = self.__step_forward(self.rear)

    def dequeue(self):
        if self.is_empty():
            raise Exception("The queue is Empty")
        ret = self.container[self.front]
        self.front = self.__step_forward(self.front)
        return ret

    def peek(self):
        if self.is_empty():
            raise Exception("The queue is Empty")
        return self.container[self.front]


cq = CQueue()

for i in range(8):
    cq.enqueue(i)

for i in range(5):
    print(cq.dequeue(), end = ' ')

for i in range(8, 14):
    cq.enqueue(i)

while not cq.is_empty():
    print(cq.dequeue(), end = ' ')

print()
for i in range(10):
    print(cq.container[i], end = ' ')