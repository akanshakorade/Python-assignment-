import multiprocessing
import os

def CountOdd(N):
    count = (N + 1) // 2

    print("Process ID :", os.getpid())
    print("Input Number :", N)
    print("Odd Number Count :", count)
    print()

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()
    p.map(CountOdd, Data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()