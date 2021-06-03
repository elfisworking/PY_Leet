class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.num = 0


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        self.num += 1


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.num -= 1
        if len(self.stack2) != 0:
            return self.stack2.pop()
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """  
        if len(self.stack2) != 0:
            return self.stack2[-1]
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.num == 0:
            return True
        return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()