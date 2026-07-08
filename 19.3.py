from functools import reduce

Data = list(map(int, input("Enter numbers: ").split()))

FilterData = list(filter(lambda No: 70 <= No <= 90, Data))
print("List after filter =", FilterData)

MapData = list(map(lambda No: No + 10, FilterData))
print("List after map =", MapData)

if len(MapData) > 0:
    Result = reduce(lambda A, B: A * B, MapData)
    print("Output of reduce =", Result)
else:
    print("No numbers found between 70 and 90.")