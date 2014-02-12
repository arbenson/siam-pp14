import random, numpy, hadoopy
class SerialTSQR:
  def __init__(self, blocksize, isreducer):
    self.bsize, self.data = blocksize, []
    self.__call__ = self.reducer if isreducer else self.mapper

  def compress(self):
    R = numpy.linalg.qr(numpy.array(self.data), 'r')
    self.data = [[float(v) for v in row] for row in R]
    
  def collect(self,key,value):
    self.data.append(value)
    if len(self.data) > self.bsize * len(self.data[0]):
      self.compress()

  def close(self):
    self.compress()
    for row in self.data: yield random.randint(0,2000000000), row
            
  def mapper(self,key,value):
    self.collect(key,value)
        
  def reducer(self,key,values):
    for value in values: self.mapper(key,value)
           
if __name__=='__main__':
  mapper = SerialTSQR(blocksize=3, isreducer=False)
  reducer = SerialTSQR(blocksize=3, isreducer=True)
  hadoopy.run(mapper, reducer)
