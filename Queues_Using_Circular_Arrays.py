class CIRCULARARRAYQUEUE:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * CIRCULARARRAYQUEUE.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        item_to_dequeue = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return item_to_dequeue

    def enqueue(self, element):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        back_of_the_queue = (self._front + self._size) % len(self._data)
        self._data[back_of_the_queue] = element
        self._size += 1

    def _resize(self, new_capacity):
        old_data = self._data
        self._data = [None] * new_capacity
        current_index = self._front
        for item in range(self._size):
            self._data[item] = old_data[current_index]
            current_index = (current_index + 1) % len(old_data)
        self._front = 0


class Empty(Exception):
    pass
if __name__ == "__main__":
    q = CIRCULARARRAYQUEUE()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("First:", q.first())   # Should print 10
    print("Dequeue:", q.dequeue())  # Should remove 10
    print("First now:", q.first())  # Should now be 20
    print("Length:", len(q))    # Should be 2
