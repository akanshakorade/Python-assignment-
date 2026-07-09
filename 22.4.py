import multiprocessing
import time

def SumPower(N):
    Total = 0

    for i in range(1, N + 1):
        Total += i ** 5

    return Total

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    Start = time.time()

    p = multiprocessing.Pool()

    Result = p.map(SumPower, Data)

    p.close()
    p.join()

    End = time.time()

    print(Result)
    print("Execution Time :", End - Start)

if __name__ == "__main__":
    main()