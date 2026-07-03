def Check(No):
    if No % 3 == 0 and No % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

def main():
    Num = int(input("Enter number: "))
    Check(Num)

if __name__ == "__main__":
    main()