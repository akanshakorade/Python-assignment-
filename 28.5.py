def SearchWord(FileName, Word):
    try:
        fobj = open(FileName, "r")
        
        Data = fobj.read()

        if Word in Data:
            print("Word found")
        else:
            print("Word not found")
        fobj.close()    
    except FileNotFoundError:
        print("File not found")
    

def main():
    Name = input("Enter file name : ")
    Word = input("Enter Word :")
    SearchWord(Name, Word)


if __name__ == "__main__":
    main()