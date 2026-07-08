import threading

def EvenList(arr):
    even = []
    s = 0

    for i in arr:
        if i % 2 == 0:
            even.append(i)
            s += i

    print("Even Elements:", even)
    print("Sum of Even Elements:", s)

def OddList(arr):
    odd = []
    s = 0

    for i in arr:
        if i % 2 != 0:
            odd.append(i)
            s += i

    print("Odd Elements:", odd)
    print("Sum of Odd Elements:", s)

arr = list(map(int, input("Enter elements: ").split()))

t1 = threading.Thread(target=EvenList, args=(arr,))
t2 = threading.Thread(target=OddList, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()