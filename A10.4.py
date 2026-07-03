def SumNatural(No):
    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + i

    return Sum

def main():
    Num = int(input("Enter number: "))
    Ans = SumNatural(Num)
    print("Addition is:", Ans)

if __name__ == "__main__":
    main()