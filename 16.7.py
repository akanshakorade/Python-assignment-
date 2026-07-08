def ChkNum(no):
    if no % 5 == 0:
        return True
    else:
        return False

value = int(input("Enter number: "))

result = ChkNum(value)
print(result)