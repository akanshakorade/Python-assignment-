from functools import reduce

def Prime(No):
    if No < 2:
        return False

    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False

    return True

Data = list(map(int, input("Enter numbers : ").split()))

FilterData = list(filter(Prime, Data))
print("List after filter =", FilterData)

MapData = list(map(lambda No: No * 2, FilterData))
print("List after map =", MapData)

if len(MapData) > 0:
    Result = reduce(lambda A, B: A if A > B else B, MapData)
    print("Output of reduce =", Result)
else:
    print("No prime numbers found.")