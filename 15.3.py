def main():
    Data = list(map(int, input("Enter numbers : ").split()))

    Result = list(filter(lambda No: No % 2 != 0, Data))

    print("Output :", Result)

if __name__ == "__main__":
    main()