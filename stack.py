class Stack:
    def __init__(self):
        self.pointer = -1
        self.arr = []

    def push(self, item):
        self.pointer += 1
        self.arr.append(item)

    def remove(self):
        self.arr.remove(self.arr[self.pointer])
        if self.pointer == 0 and self.arr:
            pass
        else:
            self.pointer -= 1

    def down(self):
        if self.pointer == 0:
            raise Exception('/n Already at the bottom of the stack')
        self.pointer -= 1

    def up(self):
        if self.pointer+1 == len(self.arr):
            raise Exception('/n Already at the top of the stack')
        self.pointer += 1

    def index(self, i):
        if type(i) is not int:
            raise Exception('/n Index needs to be an int')
        if i < 0 or i >= len(self.arr):
            raise Exception('/n Index out of bounds')
        self.pointer = i

    def look(self):
        if self.pointer == -1:
            raise Exception('\n No vars to return')
        return self.arr(self.pointer)

    def print(self):
        if self.pointer == -1:
            raise Exception('\n No vars to print')
        print(self.arr[self.pointer])

    def print_stack(self):
        if self.pointer == -1:
            raise Exception('\n No vars to print')
        print(self.arr)
