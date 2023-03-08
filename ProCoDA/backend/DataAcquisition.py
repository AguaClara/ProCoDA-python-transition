import Buffer


class DataAcquisition:
    def __init__(self, size=100, ):
        self.buffer = Buffer(size)

        # there are 5 pumps
        self.coag = "placeholder"
        self.PAC = "placeholder"
        self.water = "placeholder"
        self.humic_acid = "placeholder"
        self.waste = "placeholder"

        # there are 2 sensors
        self.influent_turbidity = "placeholder"
        self.effluent = "placeholder"

    def read_data(self, num_samples=100):
        pass
