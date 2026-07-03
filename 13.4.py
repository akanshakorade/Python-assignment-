def Palindrome(No):
    Temp = No
    Rev = 0

    while Temp > 0:
        Digit = Temp % 10
        Rev = Rev * 10 + Digit
        Temp = Temp // 10

    if Rev == No:
        print("Palindrome Number")
    else:
        print("Not Palindrome Number")

def main():
    Num = int(input("Enter number: "))
    Palindrome(Num)

if __name__ == "__main__":
    main()