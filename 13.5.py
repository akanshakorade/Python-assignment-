def Armstrong(No):
    Temp = No
    Sum = 0

    while Temp > 0:
        Digit = Temp % 10
        Sum = Sum + (Digit ** 3)
        Temp = Temp // 10

    if Sum == No:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")

def main():
    Num = int(input("Enter number: "))
    Armstrong(Num)

if __name__ == "__main__":
    main()