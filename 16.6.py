def ChkNum(no):
    if no > 0:
        print("Positive Number")
    elif no < 0:
        print("Negative Number")
    else:
        print("Zero")

value = int(input("Enter number: "))
ChkNum(value)