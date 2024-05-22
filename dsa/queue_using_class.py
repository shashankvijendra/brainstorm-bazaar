class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Queue is empty!")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty!")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
if __name__ == "__main__":
    my_queue = Queue()
    my_queue.enqueue('apple')
    my_queue.enqueue('banana')
    my_queue.enqueue('cherry')

    print(f"Queue size: {my_queue.size()}")
    print(f"Front element: {my_queue.peek()}")

    dequeued_item = my_queue.dequeue()
    print(f"Dequeued item: {dequeued_item}")
    print(f"Queue size after dequeueing: {my_queue.size()}")
