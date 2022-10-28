class DataAqusition:
    data = {}

    def __init__(self):
        self.data = {}

    @classmethod
    def set_data(cls, data):
        DataAqusition.data = data

    def read_data(self):
        # implement a function to read data in from somewhere and set our class var
        pass
