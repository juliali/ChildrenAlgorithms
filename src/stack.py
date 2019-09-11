class Stack:

    data = []
    top = -1

    
    def __init__(self):
        self.data = list()
        self.top = -1
        return


    def push(self, element):
        self.data.append(element)
        self.top += 1
        return

    def pop(self):
        if self.top < 0:
            print("Warning：Stack Empty!")
            return None
        else:
            element = self.data[self.top]
            self.data.remove(element)
            self.top -= 1
            return element

    def size(self):
        return self.top + 1


if __name__ == "__main__":

    myStack = Stack()

    print("size:", myStack.size())

    myStack.push("apple")
    myStack.push("banana")
    myStack.push("cherry")

    print(myStack.pop())
    print(myStack.pop())
    print("size:", myStack.size())
    print(myStack.pop())
    print("size:", myStack.size())
    print(myStack.pop())
    print("size:", myStack.size())