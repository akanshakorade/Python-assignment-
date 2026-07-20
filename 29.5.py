def Frequency(FileName, Word):
    try:
        fobj = open(FileName, "r")

        Data = fobj.read()

        Count = Data.count(Word)

        print("Frequency :", Count)

        fobj.close()

    except FileNotFoundError:
        print("File not found")

def main():
    Name = input("Enter file name : ")
    Word = input("Enter word : ")

    Frequency(Name, Word)

if __name__ == "__main__":
    main()