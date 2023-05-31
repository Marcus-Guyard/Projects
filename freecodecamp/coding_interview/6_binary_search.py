path = []
def binarySearch(searchList, value):
  if not searchList:
    return "Value Not Found"
  x = len(searchList) - 1
  halfx = x // 2
  middle_value = searchList[halfx]
  greater = [c for c in searchList if c > middle_value]
  lesser = [c for c in searchList if c < middle_value]

  if middle_value == value:
    return path
  if middle_value < value:
    return path + binarySearch(greater, value)
  if middle_value > value:
    return path + binarySearch(lesser, value)