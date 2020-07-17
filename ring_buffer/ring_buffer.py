class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0 #This will help see what element should be removed

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage.pop(self.index)
            self.storage.insert(self.index,item)
            self.index+=1
            if self.index >= self.capacity:
                self.index = 0

    def get(self):
        return self.storage



rb = RingBuffer(3)

rb.append("a")
rb.append("b")
rb.append("c")
print(rb.get())
rb.append("d")
print(rb.get())
rb.append('e')
rb.append('f')
print(rb.get())

