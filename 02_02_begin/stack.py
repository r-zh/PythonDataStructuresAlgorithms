"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""


class Stack:
    # in the empty class, we must write pass to avoid error
    # pass

    def __init__(self):
        self.items = []

    def is_empty(self):
        # return len(self.items) == 0 '
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items(-1)

    def size(self):
        return len(self.items)

    # works for the print function
    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s)
    print(2 ^ 11 ^ 2)
