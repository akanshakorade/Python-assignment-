from functools import reduce

Data = list(map(int, input("Enter numbers : ").split()))

FilterData = list(filter(lambda No: No % 2 == 0, Data))
print("List after filter =", FilterData)

MapData = list(map(lambda No: No * No, FilterData))
print("List after map =", MapData)

Result = reduce(lambda A, B: A + B, MapData)

print("Output of reduce =", Result)