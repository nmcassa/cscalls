class Stack:
    def __init__(self):
        self.pointer = -1
        self.arr = []

    def push(self, item):
        self.pointer += 1
        self.arr.append(item)

    def print(self):
        if self.pointer == -1:
            raise Exception('\n No vars to print')
        print(self.arr[self.pointer])
