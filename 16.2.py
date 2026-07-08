def ChkNum(no):
    if no % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

value = int(input("Enter number: "))
ChkNum(value)