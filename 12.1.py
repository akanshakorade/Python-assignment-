def MultFactors(No):
    Mult = 1

    for i in range(1, No + 1):
        if No % i == 0:
            Mult = Mult * i

    print("Multiplication of factors is:", Mult)

def main():
    Num = int(input("Enter number: "))
    MultFactors(Num)

if __name__ == "__main__":
    main()