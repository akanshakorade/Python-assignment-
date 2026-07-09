import multiprocessing
import os

def CountEven(N):
    count = N // 2

    print("Process ID :", os.getpid())
    print("Input Number :", N)
    print("Even Number Count :", count)
    print()

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()
    p.map(CountEven, Data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()