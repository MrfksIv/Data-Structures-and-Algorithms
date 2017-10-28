# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []
    self.size = None


  def ReadData(self):
    n = int(input())
    # print("parasr", n)
    self._data = [int(s) for s in input().split()]
    self.size = len(self._data)
    assert n == self.size

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def siftDown(self, i):
    leftChildIndex = i * 2 + 1
    rightChildIndex = i * 2 + 2
    minIndex = i
    # print('minIndex: {}'.format(minIndex))

    if leftChildIndex < self.size and self._data[leftChildIndex] < self._data[minIndex]:
      minIndex = leftChildIndex

    if rightChildIndex < self.size  and self._data[rightChildIndex] < self._data[minIndex]:
      minIndex = rightChildIndex

    if i != minIndex and minIndex < self.size:
      self._swaps.append((i, minIndex))
      self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
      self.siftDown(minIndex)

  # def buildHeap(self):
  #   for i in range(self.size/2, 1):
  #     temp = self._data[0]
  #     self._data[0] = self._data[tmpSize]
  #     self.size -= 1
  #     tmpSize = self.siftDown(0)

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(int(len(self._data) / 2), -1, -1):
      # print(i)
      self.siftDown(i)


  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()

    # heap_builder._data = [5, 4, 3, 2, 1]
    # heap_builder.size = len(heap_builder._data)

    heap_builder.Solve()
