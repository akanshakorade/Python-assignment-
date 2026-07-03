def SumDigits(No):
    Sum = 0

    while No > 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    print("Sum of digits is:", Sum)

def main():
    Num = int(input("Enter number: "))
    SumDigits(Num)

if __name__ == "__main__":
    main()