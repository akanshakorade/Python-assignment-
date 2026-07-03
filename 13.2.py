def SumDigits(No):
    Sum = 0

    while No > 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    Num = int(input("Enter number: "))
    Ans = SumDigits(Num)
    print("Sum of digits:", Ans)

if __name__ == "__main__":
    main()