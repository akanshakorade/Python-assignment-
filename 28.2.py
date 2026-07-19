def CountWords(Filename):
    try:
        fobj = open(Filename, "r")
        count = 0
        
        for words in fobj:
            count += len(words.split())
            
        fobj.close()
        return count
    except FileNotFoundError:
        return "File not found"
def main():
    Name = input("Enter file name :")
    Ret = CountWords(Name)
    print("Total number of words :",Ret)

if __name__ == "__main__":
    main()
        