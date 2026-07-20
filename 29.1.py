import os
def CheckFile(FileName):
    if os.path.exists(FileName):
        print("Filebdoes not exist")

def main():
    Name = input("Enter file name:")
    CheckFile(Name)

if __name__ == "__main__":
    main()        