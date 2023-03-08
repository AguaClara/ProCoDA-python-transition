import numpy as np

class Buffer:

    def __init__(self, size = 100):
        self.buffer = np.zeros(size)
        self.size = size

    def read_average(self):
        return self.buffer.sum() / self.size

    def read_recent(self):
        return self.buffer[self.size - 1]

    def read_all(self):
        return self.buffer.deepcopy()

    def set_buffer_size(self, size):
        self.size = size
        new = np.zeros(size)
        for i in range(len(self.buffer)):
            new[i] = self.buffer[i]

    def read_channel_config(self):
        pass

    def write_channel_config(self):
        pass

    def clear(self):
        self.buffer = np.zeros(self.size)

    def write(self,data):
        self.buffer.append(data)

    def write(self, data):
        self.buffer = np.concatenate(self.buffer, data)

