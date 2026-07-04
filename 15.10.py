def main():
    Data = list(map(int, input("Enter numbers : ").split()))

    Result = list(filter(lambda No: No % 2 == 0, Data))

    print("Count of Even Numbers :", len(Result))

if __name__ == "__main__":
    main()