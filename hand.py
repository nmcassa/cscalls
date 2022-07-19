class Hand:
    def __init__(self):
        self.val = None

    def set(self, var):
        self.val = var

    def get(self):
        if self.val is None:
            raise Exception('/n Nothing is being held')
        return self.val

    def print(self):
        if self.val is None:
            raise Exception('/n Nothing is being held')
        print(self.val)
