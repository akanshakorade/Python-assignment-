import multiprocessing
import math
import os

def Factorial(N):
    print("Process ID :", os.getpid())
    print("Input Number :", N)
    print("Factorial :", math.factorial(N))
    print()

def main():
    Data = [10, 15, 20, 25]

    p = multiprocessing.Pool()
    p.map(Factorial, Data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()