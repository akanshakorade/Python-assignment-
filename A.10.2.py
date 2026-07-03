def MultFactors(No):
    Mult = 1

    for i in range(1, No):
        if No % i == 0:
            Mult = Mult * i

    return Mult

def main():
    Num = int(input("Enter number: "))
    Ans = MultFactors(Num)
    print("Multiplication of factors is:", Ans)

if __name__ == "__main__":
    main()