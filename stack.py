class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self): # If print; get the information returned
        return str(self.items)


if __name__ == '__main__':
    s = Stack()
    print(s)