def CountDigits(No):
    Count = 0

    while No > 0:
        Count = Count + 1
        No = No // 10

    print("Number of digits is:", Count)

def main():
    Num = int(input("Enter number: "))
    CountDigits(Num)

if __name__ == "__main__":
    main()