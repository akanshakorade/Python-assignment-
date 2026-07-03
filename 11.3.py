def SumFactors(No):
    Sum = 0

    for i in range(1, No + 1):
        if No % i == 0:
            Sum = Sum + i

    return Sum

def main():
    Num = int(input("Enter number: "))
    Ans = SumFactors(Num)
    print("Sum of factors is:", Ans)

if __name__ == "__main__":
    main()