import sys

def CopyFile(Source):
    try:
        fsrc = open(Source, "r")
        fdest = open("Demo.txt","w")

        Data = fsrc.read()
        fdest.write(Data)

        fsrc.close()
        fdest.close()

        print("Contents copied successfully")

    except FileNotFoundError:
        print("File not found")

def main():
    CopyFile(sys.argv[1])

if __name__ == "__main__":
    main()            

