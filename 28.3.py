def Display(Filename):
    try:
        fobj = open(Filename, "r")
        
        for line in fobj:
            print(line, end="")
            
        fobj.close()
        
    except FileNotFoundError:
        return "File not found"
def main():

    Name = input("Enter file name :")
    Display(Name)
    

if __name__ == "__main__":
    main()
        