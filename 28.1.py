def Countlines(Filename):
    try:
        fobj = open(Filename, "r")
        count = 0
        for line in fobj:
            count += len(line.split())
            
        fobj.close()
        return count
    except FileNotFoundError:
        return "File not found"
def main():
    Display()
    print("Contents of the file line by line:")
    Name = input("Enter file name :")
    Ret = Countlines(Name)
    print("Total number of lines :",Ret)
if __name__ == "__main__":
    main()
        