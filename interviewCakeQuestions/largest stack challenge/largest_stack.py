from collections import deque


class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]
# =======================================================

# My code:


class MaxStack(Stack):
    def __init__(self):
        super().__init__()
        self.stackOfHighestNums = deque()

    def push(self, item):
        if item >= self.stackOfHighestNums[-1]:
            self.stackOfHighestNums.append(item)
        super().push(item)

    def pop(self):
        if self.peek() == self.stackOfHighestNums[-1]:
            self.stackOfHighestNums.pop()
        super().pop()

    def get_max(self):
        print(self.stackOfHighestNums[-1])
