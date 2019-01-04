# ======= assumption: Stack class is already given (copied the code stub from the 'largest stack' challenge) ===========

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

class queue(): 
    def __init__(self):
        self.stack1Linear = Stack()
        self.stack2Reversed = Stack()

    def enqueue(self,item):
        self.stack1Linear.push(item)
    
    def dequeue(self):
        if self.stack2Reversed.peek() is None:
            self.copyProcedure()
            
        return self.stack2Reversed.pop()
    
    def copyProcedure(self):
        if self.stack1Linear.peek() is None:
            raise IndexError("Queue is empty, can't dequeue")
        while self.stack1Linear.peek() is not None:
            elem = self.stack1Linear.pop() 
            self.stack2Reversed.push(elem)