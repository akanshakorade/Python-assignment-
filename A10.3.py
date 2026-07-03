def DisplayTable(No):
    for i in range(1, 11):
        print(No * i)

def main():
    Num = int(input("Enter number: "))
    DisplayTable(Num)

if __name__ == "__main__":
    main()