# Assignment no: 14
Q1. Write a lambda function which accepts one number and returns square of that number.
square = lambda x: x * x
```python
num = int(input("Enter number: "))
print("Square =", square(num))
```
<img width="757" height="161" alt="Screenshot 2026-07-03 210636" src="https://github.com/user-attachments/assets/0a57c9e3-8d6b-46f9-97cc-e240b687bb76" />

Q2. Write a lambda function which accepts one number and returns cube of that number.
cube = lambda x: x * x * x
```python
num = int(input("Enter number: "))
print("Cube =", cube(num))
```
<img width="756" height="73" alt="Screenshot 2026-07-03 211829" src="https://github.com/user-attachments/assets/cad52063-c039-4c47-a950-deb00d1d2527" />

Q3. Write a lambda function which accepts two numbers and returns maximum number.
maximum = lambda a, b: a if a > b else b
```python
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Maximum =", maximum(x, y))
```
<img width="746" height="95" alt="Screenshot 2026-07-03 211855" src="https://github.com/user-attachments/assets/15c0978e-baf9-4cd6-9550-fd0de35f7d57" />

Q4. Write a lambda function which accepts two numbers and returns minimum number.
minimum = lambda a, b: a if a < b else b
```python
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Minimum =", minimum(x, y))
```
<img width="760" height="91" alt="Screenshot 2026-07-03 212039" src="https://github.com/user-attachments/assets/7ee979db-e946-48c5-a750-6f2bde002550" />

Q5. Write a lambda function which accepts one number and returns True if number is even otherwise False.
even = lambda x: x % 2 == 0
```python
num = int(input("Enter number: "))
print(even(num))
```
<img width="770" height="68" alt="Screenshot 2026-07-03 212050" src="https://github.com/user-attachments/assets/77a01196-c9e5-4f2c-a3eb-944e06488cfe" />

Q6. Write a lambda function which accepts one number and returns True if number is odd otherwise False.
odd = lambda x: x % 2 != 0
```python
num = int(input("Enter number: "))
print(odd(num))
```
<img width="685" height="71" alt="Screenshot 2026-07-03 212101" src="https://github.com/user-attachments/assets/294ed9ac-f8b3-45da-a9bc-6caf8c57455f" />

Q7. Write a lambda function which accepts one number and returns True if divisible by 5.
```python
div5 = lambda x: x % 5 == 0

num = int(input("Enter number: "))
print(div5(num))
```
Q8. Write a lambda function which accepts two numbers and returns addition.
add = lambda a, b: a + b
```python
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition =", add(x, y))
```
Q9. Write a lambda function which accepts two numbers and returns multiplication.
```python
multiply = lambda a, b: a * b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Multiplication =", multiply(x, y))
```
Q10. Write a lambda function which accepts three numbers and returns largest number.
```python
largest = lambda a, b, c: a if a >= b and a >= c else (b if b >= c else c)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Largest =", largest(x, y, z)
```

<img width="772" height="443" alt="Screenshot 2026-07-03 212616" src="https://github.com/user-attachments/assets/be763417-aa7a-4dc9-9ae9-a04835cd2e02" />

# Assignment no: 09

Question 1

Write a program which contains one function named as Display() that prints "Jay Ganesh" on console.
```python

def Display():
    print("Jay Ganesh")

def main():
    Display()

if __name__ == "__main__":
    main()
```
Question 2

Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
```python
def ChkGreater(No1, No2):
    if No1 > No2:
        print(No1, "is greater")
    else:
        print(No2, "is greater")

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))
    ChkGreater(Value1, Value2)

if __name__ == "__main__":
    main()
```
Question 3

Write a program which accepts one number and prints square of that number.
```python

def Square(No):
    print("Square is:", No * No)

def main():
    Num = int(input("Enter number: "))
    Square(Num)

if __name__ == "__main__":
    main()
```
Question 4

Write a program which accepts one number and prints cube of that number.
```python

def Cube(No):
    print("Cube is:", No * No * No)

def main():
    Num = int(input("Enter number: "))
    Cube(Num)

if __name__ == "__main__":
    main()
```
Question 5

Write a program which accepts one number and checks whether it is divisible by 3 and 5.
```python
def Check(No):
    if No % 3 == 0 and No % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

def main():
    Num = int(input("Enter number: ")

    Check(Num)

if __name__ == "__main__":
    main()
```

<img width="801" height="536" alt="Screenshot 2026-07-03 222941" src="https://github.com/user-attachments/assets/29a09127-f95e-483a-9fa9-7f4849e95e0b" />

# Assignment no: 10

Question 1

Write a program which accepts one number from user and return addition of its factors.
```pythom

def SumFactors(No):
    Sum = 0

    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    return Sum

def main():
    Num = int(input("Enter number: "))
    Ans = SumFactors(Num)
    print("Addition of factors is:", Ans)

if __name__ == "__main__":
    main()
```
Question 2

Write a program which accepts one number from user and return multiplication of its factors.
```python

def MultFactors(No):
    Mult = 1

    for i in range(1, No):
        if No % i == 0:
            Mult = Mult * i

    return Mult

def main():
    Num = int(input("Enter number: "))
    Ans = MultFactors(Num)
    print("Multiplication of factors is:", Ans)

if __name__ == "__main__":
    main()
```
Question 3

Write a program which accepts one number from user and display multiplication table of that number.
```python

def DisplayTable(No):
    for i in range(1, 11):
        print(No * i)

def main():
    Num = int(input("Enter number: "))
    DisplayTable(Num)

if __name__ == "__main__":
    main()
```
Question 4

Write a program which accepts one number from user and return the addition of first N natural numbers.
```python
def SumNatural(No):
    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + i

    return Sum

def main():
    Num = int(input("Enter number: "))
    Ans = SumNatural(Num)
    print("Addition is:", Ans)

if __name__ == "__main__":
    main()
```
Question 5

Write a program which accepts one number from user and return factorial of that number.
```python

def Factorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    return Fact

def main():
    Num = int(input("Enter number: "))
    Ans = Factorial(Num)
    print("Factorial is:", Ans)

if __name__ == "__main__":
    main()
```

<img width="802" height="762" alt="Screenshot 2026-07-03 225528" src="https://github.com/user-attachments/assets/080f0ed6-2c59-4256-973c-d4f58dda3746" />

# Assignment no: 11

Question 1

Write a program which accepts one number and checks whether it is a perfect number or not.
```python
def Perfect(No):
    Sum = 0

    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    if Sum == No:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

def main():
    Num = int(input("Enter number: "))
    Perfect(Num)

if __name__ == "__main__":
    main()
    ```
Question 2

Write a program which accepts one number and displays its factors.
```python
def Factors(No):
    for i in range(1, No + 1):
        if No % i == 0:
            print(i, end=" ")

def main():
    Num = int(input("Enter number: "))
    Factors(Num)

if __name__ == "__main__":
    main()
Question 3

Write a program which accepts one number and returns the addition of all its factors.
```python
def SumFactors(No):
    Sum = 0

    for i in range(1, No + 1):
        if No % i == 0:
            Sum = Sum + i

    return Sum

def main():
    Num = int(input("Enter number: "))
    Ans = SumFactors(Num)
    print("Sum of factors is:", Ans)

if __name__ == "__main__":
    main()
    ````
Question 4

Write a program which accepts one number and returns the addition of its proper factors.
```python
def SumProperFactors(No):
    Sum = 0

    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    return Sum

def main():
    Num = int(input("Enter number: "))
    Ans = SumProperFactors(Num)
    print("Sum of proper factors is:", Ans)

if __name__ == "__main__":
    main()
    ```
Question 5

Write a program which accepts one number and checks whether it is a perfect number or not using the sum of proper factors.
```python
def CheckPerfect(No):
    Sum = 0

    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    if Sum == No:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

def main():
    Num = int(input("Enter number: "))
    CheckPerfect(Num)

if __name__ == "__main__":
    main()
```

<img width="868" height="412" alt="Screenshot 2026-07-03 231141" src="https://github.com/user-attachments/assets/d520aaa0-239d-4721-ac7f-d930391988e0" />

# Assignment 12

Write a program which accepts one number and displays the multiplication of all factors of that number.
```python
def MultFactors(No):
    Mult = 1

    for i in range(1, No + 1):
        if No % i == 0:
            Mult = Mult * i

    print("Multiplication of factors is:", Mult)

def main():
    Num = int(input("Enter number: "))
    MultFactors(Num)

if __name__ == "__main__":
    main()
    ```
Question 2

Write a program which accepts one number and displays the addition of all digits of that number.
```python
def SumDigits(No):
    Sum = 0

    while No > 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    print("Sum of digits is:", Sum)

def main():
    Num = int(input("Enter number: "))
    SumDigits(Num)

if __name__ == "__main__":
    main()
    ```
Question 3

Write a program which accepts one number and displays the count of digits.
```python
def CountDigits(No):
    Count = 0

    while No > 0:
        Count = Count + 1
        No = No // 10

    print("Number of digits is:", Count)

def main():
    Num = int(input("Enter number: "))
    CountDigits(Num)

if __name__ == "__main__":
    main()
    ```
Question 4
```python

Write a program which accepts one number and displays the reverse of that number.

def Reverse(No):
    Rev = 0

    while No > 0:
        Digit = No % 10
        Rev = Rev * 10 + Digit
        No = No // 10

    print("Reverse number is:", Rev)

def main():
    Num = int(input("Enter number: "))
    Reverse(Num)

if __name__ == "__main__":
    main()
    ```
Question 5

Write a program which accepts one number and checks whether it is a palindrome or not.
```python
def Palindrome(No):
    Temp = No
    Rev = 0

    while No > 0:
        Digit = No % 10
        Rev = Rev * 10 + Digit
        No = No // 10

    if Temp == Rev:
        print("Palindrome Number")
    else:
        print("Not Palindrome Number")

def main():
    Num = int(input("Enter number: "))
    Palindrome(Num)

if __name__ == "__main__":
    main()
    ```

<img width="792" height="433" alt="Screenshot 2026-07-03 233114" src="https://github.com/user-attachments/assets/cd98c5b4-924f-4fc8-a71b-17f7e41c96b2" />
# Assignment no: 13
Question 1
```python
Write a program which accepts one number and checks whether it is an Armstrong number or not.

def Armstrong(No):
    Temp = No
    Sum = 0

    while No > 0:
        Digit = No % 10
        Sum = Sum + (Digit ** 3)
        No = No // 10

    if Temp == Sum:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")

def main():
    Num = int(input("Enter number: "))
    Armstrong(Num)

if __name__ == "__main__":
    main()
```
Question 2
```python
Write a program which accepts one number and returns the addition of even digits.

def EvenDigitSum(No):
    Sum = 0

    while No > 0:
        Digit = No % 10

        if Digit % 2 == 0:
            Sum = Sum + Digit

        No = No // 10

    print("Sum of even digits is:", Sum)

def main():
    Num = int(input("Enter number: "))
    EvenDigitSum(Num)

if __name__ == "__main__":
    main()
```
Question 3

Write a program which accepts one number and returns the multiplication of odd digits.

def OddDigitMult(No):
    Mult = 1

    while No > 0:
        Digit = No % 10

        if Digit % 2 != 0:
            Mult = Mult * Digit

        No = No // 10

    print("Multiplication of odd digits is:", Mult)

def main():
    Num = int(input("Enter number: "))
    OddDigitMult(Num)

if __name__ == "__main__":
    main()
    ```
Question 4

Write a program which accepts one number and counts the frequency of digit 2.
```python
def CountTwo(No):
    Count = 0

    while No > 0:
        Digit = No % 10

        if Digit == 2:
            Count = Count + 1

        No = No // 10

    print("Frequency of 2 is:", Count)

def main():
    Num = int(input("Enter number: "))
    CountTwo(Num)

if __name__ == "__main__":
    main()
    ```
Question 25
```python

Write a program which accepts one number and returns the difference between the summation of even digits and odd digits.

def DigitDifference(No):
    EvenSum = 0
    OddSum = 0

    while No > 0:
        Digit = No % 10

        if Digit % 2 == 0:
            EvenSum = EvenSum + Digit
        else:
            OddSum = OddSum + Digit

        No = No // 10

    print("Difference is:", EvenSum - OddSum)

def main():
    Num = int(input("Enter number: "))
    DigitDifference(Num)

if __name__ == "__main__":
    main()
```
<img width="823" height="445" alt="Screenshot 2026-07-03 235533" src="https://github.com/user-attachments/assets/9ec3e624-7526-4790-9678-acf4857239d0" />

