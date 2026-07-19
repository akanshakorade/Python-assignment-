def CopyFile(Source, Destination):
    try:
        fsrc = open(Source, "r")
        fdest = open(Destination, "w")

        Data = fsrc.read()
        fdest.write(Data)

        fsrc.close()
        fdest.close()

        print("Contents copied successfully")

    except FileNotFoundError:
        print("Source file not found")

def main():
    Src = input("Enter source file : ")
    Dest = input("Enter destination file : ")

    CopyFile(Src, Dest)

if __name__ == "__main__":
    main()