class Queue:
    data = []

    def __init__(self):
        self.data = list()
        return


    def enqueue(self, element):
        self.data.append(element)
        return

    def dequeue(self):
        if len(self.data) <= 0:
            print("Warning：Queue Empty!")
            return None
        else:
            element = self.data[0]
            self.data.remove(element)
            return element

    def size(self):
        return len(self.data)


if __name__ == "__main__":
    myQueue = Queue()

    print("size:", myQueue.size())

    myQueue.enqueue("apple")
    myQueue.enqueue("banana")
    myQueue.enqueue("cherry")

    print(myQueue.dequeue())
    print(myQueue.dequeue())
    print("size:", myQueue.size())
    print(myQueue.dequeue())
    print("size:", myQueue.size())
    print(myQueue.dequeue())
    print("size:", myQueue.size())