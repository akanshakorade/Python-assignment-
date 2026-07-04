def main():
    Data = list(map(int,input("Enter numbers : ").split()))

    Result = list(map(lambda No: No * No, Data))

    print("Output :",Result)

if __name__ == "__main__":
    main()    
