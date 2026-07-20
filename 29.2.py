
def Display(FileName):
    try:
        fobj = open(FileName, "r")
        Data = fobj.read()
        print(Data)
        fobj.close()
    except FilterNotFoundError:
        print("File not found")

def main():
    Name = input("Enter file name:")
    Display(Name)
    print("Display Name")

if __name__ == "__main__":
    main()        