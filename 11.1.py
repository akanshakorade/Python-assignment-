def Perfect(No):
    Sum = 0

    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    if Sum == No:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

def main():
    Num = int(input("Enter number: "))
    Perfect(Num)

if __name__ == "__main__":
    main()