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
```
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
```
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

Write a program which accepts one number and displays the reverse of that number.
```python
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
# Question 5

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
# Question 1

Write a program which accepts one number and checks whether it is an Armstrong number or not.

```python
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

Write a program which accepts one number and returns the addition of even digits.
```python
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
```python
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
# Question 25

# Write a program which accepts one number and returns the difference between the summation of even digits and odd digits.
```python
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
# Assignment no : 15

Question 1

Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.
```python
def main():
    Data = list(map(int, input("Enter numbers : ").split()))

    Result = list(map(lambda No: No * No, Data))

    print("Output :", Result)

if __name__ == "__main__":
    main()
```
<img width="722" height="78" alt="Screenshot 2026-07-05 024519" src="https://github.com/user-attachments/assets/1fb7a3bd-78ae-4700-90d2-2e794ad4c63d" />

Question 2

Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.
```python
def main():
    Data = list(map(int, input("Enter numbers : ").split()))

    Result = list(filter(lambda No: No % 2 == 0, Data))

    print("Output :", Result)

if __name__ == "__main__":
    main()
```
<img width="733" height="82" alt="Screenshot 2026-07-05 024615" src="https://github.com/user-attachments/assets/814a9b75-20dc-46c8-862a-81751072c511" />

Question 3

Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.
```python
def main():
    Data = list(map(int, input("Enter numbers : ").split()))

    Result = list(filter(lambda No: No % 2 != 0, Data))

    print("Output :", Result)

if __name__ == "__main__":
    main()
```
<img width="727" height="90" alt="Screenshot 2026-07-05 024717" src="https://github.com/user-attachments/assets/b32b8db3-95b8-4125-a231-6da67cc8c1e5" />

Question 4

Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce
```python
def main():
    Data = list(map(int, input("Enter numbers : ").split()))

    Result = reduce(lambda A, B: A + B, Data)

    print("Output :", Result)

if __name__ == "__main__":
    main()
```
<img width="723" height="83" alt="Screenshot 2026-07-05 024811" src="https://github.com/user-attachments/assets/367d6c1f-efc5-4f6b-af8d-c839510be31c" />

Question 5

Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce
```python
def main():
    Data = list(map(int, input("Enter numbers : ").split()))

    Result = reduce(lambda A, B: A if A > B else B, Data)

    print("Output :", Result)

if __name__ == "__main__":
    main()
```
<img width="752" height="83" alt="Screenshot 2026-07-05 024916" src="https://github.com/user-attachments/assets/aff93fb8-7265-4d9b-8abe-351653a7a74f" />

Question 6

Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

from functools import reduce
```python
def main():
    Data = list(map(int, input("Enter numbers : ").split()))

    Result = reduce(lambda A, B: A if A < B else B, Data)

    print("Output :", Result)

if __name__ == "__main__":
    main()
```
<img width="712" height="73" alt="Screenshot 2026-07-05 025006" src="https://github.com/user-attachments/assets/71d1914b-fb42-46e5-9eda-d6112493582e" />

Question 7

Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.
```python
def main():
    Data = input("Enter strings : ").split()

    Result = list(filter(lambda Str: len(Str) > 5, Data))

    print("Output :", Result)

if __name__ == "__main__":
    main()
```
<img width="702" height="80" alt="Screenshot 2026-07-05 025049" src="https://github.com/user-attachments/assets/68a27181-cef3-4a94-b90a-637df2fa2cb3" />

Question 8

Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.
```python
def main():
    Data = list(map(int, input("Enter numbers : ").split()))

    Result = list(filter(lambda No: No % 3 == 0 and No % 5 == 0, Data))

    print("Output :", Result)

if __name__ == "__main__":
    main()
```
<img width="708" height="71" alt="Screenshot 2026-07-05 025128" src="https://github.com/user-attachments/assets/5f9f7da5-528d-4de9-a322-723974651a7b" />

Question 9

Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce
```python
def main():
    Data = list(map(int, input("Enter numbers : ").split()))

    Result = reduce(lambda A, B: A * B, Data)

    print("Output :", Result)

if __name__ == "__main__":
    main()
```
<img width="718" height="92" alt="Screenshot 2026-07-05 025205" src="https://github.com/user-attachments/assets/ee19acd8-90e9-41c9-9a7e-c797d81e2c2d" />

Question 10

Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.
```python
def main():
    Data = list(map(int, input("Enter numbers : ").split()))

    Result = list(filter(lambda No: No % 2 == 0, Data))

    print("Count of Even Numbers :", len(Result))

if __name__ == "__main__":
    main()
```
<img width="738" height="97" alt="Screenshot 2026-07-05 025242" src="https://github.com/user-attachments/assets/083949b5-0d2c-4bc0-aa2e-b373bca9ea0b" />


# Assignment no :16

Q1. Write a program which contains one function named as Fun(). That function should display "Hello from Fun" on console.
```python
def Fun():
    print("Hello from Fun")

Fun()
```

Q2. Write a program which contains one function named as ChkNum() which accepts one parameter as number. If number is even then display "Even Number" otherwise display "Odd Number".
```python
def ChkNum(no):
    if no % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

value = int(input("Enter number: "))
ChkNum(value)
```

Q3. Write a program which contains one function named as Add() which accepts two numbers from user and returns addition of that two numbers.
```python
def Add(no1, no2):
    return no1 + no2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

ans = Add(num1, num2)
print("Addition is:", ans)
```

Q4. Write a program which displays 5 times "Marvellous" on screen.
```python
def Display():
    for i in range(5):
        print("Marvellous")

Display()
```

Q5. Write a program which displays 10 to 1 on screen.
```python
def Display():
    for i in range(10, 0, -1):
        print(i)

Display()
```


Q6. Write a program which accepts one number from user and checks whether it is Positive, Negative or Zero.
```python
def ChkNum(no):
    if no > 0:
        print("Positive Number")
    elif no < 0:
        print("Negative Number")
    else:
        print("Zero")

value = int(input("Enter number: "))
ChkNum(value)
```

Q7. Write a program which contains one function that accepts one number from user and returns True if number is divisible by 5 otherwise returns False.
```python
def ChkNum(no):
    if no % 5 == 0:
        return True
    else:
        return False

value = int(input("Enter number: "))

result = ChkNum(value)
print(result)
```

Q8. Write a program which accepts one number from user and prints that number of "*" on screen.
```python
def Display(no):
    for i in range(no):
        print("*", end=" ")

value = int(input("Enter number: "))
Display(value)
```

Q9. Write a program which displays first 10 even numbers on screen.
```python
def Display():
    for i in range(2, 21, 2):
        print(i, end=" ")

Display()
```

Q10. Write a program which accepts name from user and displays length of its name.
```python
def NameLength(name):
    return len(name)

name = input("Enter your name: ")

length = NameLength(name)
print("Length of name is:", length)
```

<img width="797" height="967" alt="Screenshot 2026-07-08 214341" src="https://github.com/user-attachments/assets/6f272568-2f18-4943-8bc6-c1cabb723d8b" />
<img width="1051" height="298" alt="Screenshot 2026-07-08 214408" src="https://github.com/user-attachments/assets/481d6b00-9419-4113-96ce-90a26ae04eaf" />

Question 1

Write a program which contains one lambda function which accepts one parameter and returns power of two.

Code
```python
Power = lambda No: No ** 2

Value = int(input("Enter number : "))

Ans = Power(Value)

print("Output :", Ans)
```
Question 2

Write a program which contains one lambda function which accepts two parameters and returns its multiplication.

Code
```python
Multiplication = lambda A, B: A * B

No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))

Ans = Multiplication(No1, No2)

print("Output :", Ans)
```
Question 3

Write a program which contains filter(), map() and reduce(). Accept a list of numbers from the user. Filter numbers greater than or equal to 70 and less than or equal to 90. Increase each filtered number by 10 using map(). Return the product of all numbers using reduce().

Code
```python
from functools import reduce

Data = list(map(int, input("Enter numbers : ").split()))

FilterData = list(filter(lambda No: No >= 70 and No <= 90, Data))
print("List after filter =", FilterData)

MapData = list(map(lambda No: No + 10, FilterData))
print("List after map =", MapData)

Result = reduce(lambda A, B: A * B, MapData)

print("Output of reduce =", Resultt
```
Question 4

Write a program which contains filter(), map() and reduce(). Accept a list of numbers from the user. Filter all even numbers. Calculate the square of each number using map(). Return the addition of all numbers using reduce().

Code
```python
from functools import reduce

Data = list(map(int, input("Enter numbers : ").split()))

FilterData = list(filter(lambda No: No % 2 == 0, Data))
print("List after filter =", FilterData)

MapData = list(map(lambda No: No * No, FilterData))
print("List after map =", MapData)

Result = reduce(lambda A, B: A + B, MapData)

print("Output of reduce =", Result)
```
Question 5

Write a program which contains filter(), map() and reduce(). Accept a list of numbers from the user. Filter all prime numbers. Multiply each number by 2 using map(). Return the maximum number using reduce().

Code
```python
from functools import reduce

def Prime(No):
    if No < 2:
        return False

    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False

    return True

Data = list(map(int, input("Enter numbers : ").split()))

FilterData = list(filter(Prime, Data))
print("List after filter =", FilterData)

MapData = list(map(lambda No: No * 2, FilterData))
print("List after map =", MapData)

Result = reduce(lambda A, B: A if A > B else B, MapData)

print("Output of reduce =", Result)
```

Question 6

Write a program which creates two threads named evenlist and oddlist. Both threads accept a list of integers as a parameter. Evenlist adds all even elements from the list, while Oddlist adds all odd elements. Display both sums.

Code
```python
import threading

def EvenList(Data):
    Sum = 0
    for No in Data:
        if No % 2 == 0:
            Sum += No
    print("Sum of even numbers :", Sum)

def OddList(Data):
    Sum = 0
    for No in Data:
        if No % 2 != 0:
            Sum += No
    print("Sum of odd numbers :", Sum)

Data = list(map(int, input("Enter numbers : ").split()))

T1 = threading.Thread(target=EvenList, args=(Data,))
T2 = threading.Thread(target=OddList, args=(Data,))

T1.start()
T2.start()

T1.join()
T2.join()
```
Question 7

Write a program which creates two threads. One thread displays factors of a number, and the other displays the sum of factors. Accept the number from the user.

Code
```python
import threading

def Factors(No):
    print("Factors are :")
    for i in range(1, No + 1):
        if No % i == 0:
            print(i)

def SumFactors(No):
    Sum = 0
    for i in range(1, No + 1):
        if No % i == 0:
            Sum += i
    print("Sum of factors :", Sum)

Value = int(input("Enter number : "))

T1 = threading.Thread(target=Factors, args=(Value,))
T2 = threading.Thread(target=SumFactors, args=(Value,))

T1.start()
T2.start()

T1.join()
T2.join()
```
<img width="941" height="892" alt="Screenshot 2026-07-08 224208" src="https://github.com/user-attachments/assets/098a473c-76cf-4bdb-a8c2-f02f2248d77d" />
<img width="777" height="938" alt="Screenshot 2026-07-08 224323" src="https://github.com/user-attachments/assets/cc41d255-e312-4137-b99f-6dd6fdfe54a0" />
<img width="98" height="911" alt="Screenshot 2026-07-08 224340" src="https://github.com/user-attachments/assets/a69db964-b63a-4d61-a033-4a532d3756cb" />

# Assignment no : 21

Question 1:

Design a Python application that creates two separate threads named Even and Odd.

Even thread should display first 10 even numbers.
Odd thread should display first 10 odd numbers.
Code:
```python
import threading

def Even():
    print("First 10 Even Numbers:")
    for i in range(2, 21, 2):
        print(i)

def Odd():
    print("First 10 Odd Numbers:")
    for i in range(1, 20, 2):
        print(i)

t1 = threading.Thread(target=Even, name="Even")
t2 = threading.Thread(target=Odd, name="Odd")

t1.start()
t2.start()

t1.join()
t2.join()
```
Question 2:

Design a Python application that creates two threads named EvenFactor and OddFactor.

Accept one integer.
EvenFactor thread displays even factors and their sum.
OddFactor thread displays odd factors and their sum.
After completion display "Exit from main".
Code:
```python
import threading

def EvenFactor(no):
    s = 0
    print("Even Factors:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i)
            s += i
    print("Sum of Even Factors:", s)

def OddFactor(no):
    s = 0
    print("Odd Factors:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i)
            s += i
    print("Sum of Odd Factors:", s)

num = int(input("Enter number: "))

t1 = threading.Thread(target=EvenFactor, args=(num,))
t2 = threading.Thread(target=OddFactor, args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")
```
Question 3:

Design a Python application that creates two threads named EvenList and OddList.

Accept a list of integers.
EvenList thread displays even numbers and their sum.
OddList thread displays odd numbers and their sum.
Code:
```python
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
```
Question 4:

Design a Python application that creates three threads named Small, Capital and Digits.

Accept a string.
Count lowercase, uppercase and digits.
Display Thread ID and Thread Name.
Code:
```python
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
```
Question 5:

Design a Python application that creates two threads named Thread1 and Thread2.

Thread1 displays numbers 1 to 50.
Thread2 displays numbers 50 to 1.
Thread2 starts only after Thread1 completes.
Code:
```python
import threading

def Thread1():
    print("Numbers from 1 to 50:")
    for i in range(1, 51):
        print(i)

def Thread2():
    print("Numbers from 50 to 1:")
    for i in range(50, 0, -1):
        print(i)

t1 = threading.Thread(target=Thread1)
t2 = threading.Thread(target=Thread2)

t1.start()
t1.join()

t2.start()
t2.join()
```
<img width="737" height="422" alt="Screenshot 2026-07-08 225518" src="https://github.com/user-attachments/assets/f6b5ef89-b0e4-40c1-8a65-5ca20692e856" />

# Assignment no: 22

Question 1

Write a Python program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.

Input

Data = [1000000, 2000000, 3000000, 4000000]
import multiprocessing
```python
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
```
Question 2

Write a Python program that calculates factorials of multiple numbers simultaneously using Pool.map().

Input

Data = [10, 15, 20, 25]

Display

Process ID
Input Number
Factorial
import multiprocessing
import math
import os
```python
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
```
Question 3

Write a Python program that accepts a list of integers and uses multiprocessing.Pool to count how many prime numbers exist between 1 and N for every element in the list.

Input

Data = [10000, 20000, 30000, 40000]
import multiprocessing
```python
def IsPrime(No):
    if No < 2:
        return False

    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False

    return True

def PrimeCount(N):
    Count = 0

    for i in range(2, N + 1):
        if IsPrime(i):
            Count += 1

    print("Prime Count up to", N, ":", Count)

def main():
    Data = [10000, 20000, 30000, 40000]

    p = multiprocessing.Pool()

    p.map(PrimeCount, Data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()
```

Question 4

Write a Python program that accepts a list of integers and uses multiprocessing.Pool to calculate the sum of 1⁵ + 2⁵ + 3⁵ + ... + N⁵ for every element in the list. Also display the total execution time.

Input

Data = [1000000, 2000000, 3000000, 4000000]
import multiprocessing
import time

```python
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
```
<img width="1907" height="746" alt="Screenshot 2026-07-09 143727" src="https://github.com/user-attachments/assets/ae98543b-8a9d-4b32-8ca8-28b727f7e5c6" />



