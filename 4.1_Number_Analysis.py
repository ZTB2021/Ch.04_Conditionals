'''
NUMBER ANALYSIS PROGRAM
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero
3.) inclusively between -100 and +100

A small report will then be printed. Use the following to test your program:

In: 32  
Out:  Test 1: Even
      Test 2: Positive
      Test 3: Inclusive

In: -123  
Out:  Test 1: Odd
      Test 2: Negative
      Test 3: Exclusive
'''
x = float(input("What is the number"))
if x % 2 == 1:
    print("The number is odd")
else:
    print("The number is even")
if x < 0:
    print("It is negative")
elif x > 0:
    print("It is positive")
else:
    print("It is zero")
if x<=100 and x>=-100:
    print("It is inclusive")
else:
    print("It is Exclusive")