import Buffer
import nidaqmx
from nidaqmx.stream_readers import (
    AnalogSingleChannelReader, AnalogMultiChannelReader)

class DataAcquisition:
  def __init__(self, size=100):
      self.buffer = Buffer(size)

  def read_data(self, num_samples=100):
    with nidaqmx.Task() as task:
      # I don't really understand the device naming stuff
        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        reader = AnalogSingleChannelReader(task.in_stream)
        values_read = []
        # how many samples do we want?
        for i in range(num_samples):
          value_read = reader.read_one_sample()
          assert isinstance(value_read, float)
          values_read.append(value_read)
        
        self.buffer.write(values_read)

