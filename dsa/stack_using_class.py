class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty!")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty!")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    print(f"Stack size: {my_stack.size()}")
    print(f"Top element: {my_stack.peek()}")

    popped_item = my_stack.pop()
    print(f"Popped item: {popped_item}")
    print(f"Stack size after popping: {my_stack.size()}")
