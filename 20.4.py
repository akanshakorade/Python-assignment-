import threading

def Small(s):
    c = 0
    for ch in s:
        if ch.islower():
            c += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Lowercase Count:", c)

def Capital(s):
    c = 0
    for ch in s:
        if ch.isupper():
            c += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Uppercase Count:", c)

def Digits(s):
    c = 0
    for ch in s:
        if ch.isdigit():
            c += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Digit Count:", c)

str1 = input("Enter string: ")

t1 = threading.Thread(target=Small, args=(str1,), name="Small")
t2 = threading.Thread(target=Capital, args=(str1,), name="Capital")
t3 = threading.Thread(target=Digits, args=(str1,), name="Digits")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()