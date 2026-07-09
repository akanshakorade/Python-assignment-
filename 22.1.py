import multiprocessing

def SumSquares(N):
    total = 0
    for i in range(1, N + 1):
        total += i * i
    return total

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()
    Result = p.map(SumSquares, Data)

    p.close()
    p.join()

    print(Result)

if __name__ == "__main__":
    main()