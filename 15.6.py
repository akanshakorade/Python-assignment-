from functools import reduce

def main():
    Data = list(map(int, input("Enter numbers : ").split()))

    Result = reduce(lambda A, B: A if A < B else B, Data)

    print("Output :", Result)

if __name__ == "__main__":
    main()