#stack in OOPs
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items)==0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an Empty Stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty Stack")

    def size(self):
        return len(self.items)

stack=Stack()
print("Is the Stack Empty?", stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.items)
print("Top of the Stack:", stack.peek())
print("Pop", stack.pop())










































