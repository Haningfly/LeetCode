class CircularQueue(object):
    def __init__(self, size):
        self.front = 0
        self.rear = 0
        self.size = size
        self.queue = [None] * size

    def is_full(self):
        if (self.rear + 1) % self.size == self.front:
            return True
        else:
            return False

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.is_full():
            return None

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        if self.is_empty():
            return None

        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        return value