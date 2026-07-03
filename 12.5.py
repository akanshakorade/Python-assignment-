def Palindrome(No):
    Temp = No
    Rev = 0

    while No > 0:
        Digit = No % 10
        Rev = Rev * 10 + Digit
        No = No // 10

    if Temp == Rev:
        print("Palindrome Number")
    else:
        print("Not Palindrome Number")

def main():
    Num = int(input("Enter number: "))
    Palindrome(Num)

if __name__ == "__main__":
    main()