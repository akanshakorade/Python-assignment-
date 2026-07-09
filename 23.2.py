import multiprocessing
import os

def SumOdd(N):
    total = 0
    for i in range(1, N + 1, 2):
        total += i

    print("Process ID :", os.getpid())
    print("Input Number :", N)
    print("Sum of Odd Numbers :", total)
    print()

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()
    p.map(SumOdd, Data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()