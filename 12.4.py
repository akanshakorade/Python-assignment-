def Reverse(No):
    Rev = 0

    while No > 0:
        Digit = No % 10
        Rev = Rev * 10 + Digit
        No = No // 10

    print("Reverse number is:", Rev)

def main():
    Num = int(input("Enter number: "))
    Reverse(Num)

if __name__ == "__main__":
    main()