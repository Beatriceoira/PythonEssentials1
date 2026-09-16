# README — LAB 2.6.10: Operators and Expressions

## Objective

Complete a Python program to evaluate the following nested mathematical expression:

<img width="900" height="338" alt="image" src="https://github.com/user-attachments/assets/6e233f95-c452-450a-ba5a-81c8689c1535" />


The result must be assigned to the variable `y`.

## Solution

```python
x = float(input())

y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))

print(y)
```

## Explanation

The mathematical expression contains several nested fractions. In Python, parentheses are used to preserve the correct structure and order of operations.

The expression:

```python
1 / (x + 1 / (x + 1 / (x + 1 / x)))
```

is evaluated from the innermost fraction outward.

Python uses the following operators in this program:

* `/` — division
* `+` — addition
* `()` — controls the order of evaluation

## Test Results

### Test 1

Input:

```text
1
```

Output:

```text
0.6000000000000001
```

### Test 2

Input:

```text
10
```

Output:

```text
0.09901951266867294
```

### Test 3

Input:

```text
100
```

Output:

```text
0.009999000199950014
```

### Test 4

Input:

```text
-5
```

Output:

```text
-0.19258202567760344
```

## Key Concepts

* Python follows operator precedence when evaluating expressions.
* Parentheses can be used to explicitly control the order of operations.
* Nested mathematical expressions can be directly translated into Python.
* The `/` operator performs floating-point division.
* `float(input())` reads the user's input and converts it to a floating-point number.

## Conclusion

This lab demonstrates how to translate a complex mathematical expression into Python. Using parentheses carefully ensures that the nested fractions are evaluated in the correct order and produce the expected results.

# README — LAB 2.6.11: Operators and Expressions – 2

## Objective

Create a Python program that calculates the **end time** of an event.

The program receives:

* Starting hour (`0–23`)
* Starting minute (`0–59`)
* Event duration in minutes

The program then calculates and displays the ending time.

## Solution

```python
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins = mins + dura
hour = hour + mins // 60
mins = mins % 60
hour = hour % 24

print(hour, ":", mins, sep="")
```

## Explanation

### Adding the Duration

First, add the event duration to the starting minutes:

```python
mins = mins + dura
```

### Converting Minutes to Hours

The `//` operator performs integer division:

```python
hour = hour + mins // 60
```

For example:

```text
119 // 60 = 1
```

This means 119 minutes contain 1 complete hour.

### Finding the Remaining Minutes

The `%` operator gives the remainder:

```python
mins = mins % 60
```

For example:

```text
119 % 60 = 59
```

So 119 minutes becomes **1 hour and 59 minutes**.

### Keeping the Hour Between 0 and 23

The `%` operator is also used to handle events that continue into the next day:

```python
hour = hour % 24
```

For example:

```text
25 % 24 = 1
```

So hour `25` becomes `1`.

### Printing the Result

```python
print(hour, ":", mins, sep="")
```

The `sep=""` prevents spaces from being inserted between the hour, colon, and minutes.

## Test Results

### Test 1

Input:

```text
12
17
59
```

Output:

```text
13:16
```

### Test 2

Input:

```text
23
58
642
```

Output:

```text
10:40
```

### Test 3

Input:

```text
0
1
2939
```

Output:

```text
1:0
```

## Key Concepts

* `//` — integer division
* `%` — modulo/remainder
* `+` — addition
* `int()` — converts input to an integer
* `sep=""` — removes separators between `print()` arguments
* `% 24` — keeps the hour within a 24-hour clock

## Conclusion

This lab demonstrates how arithmetic operators can be combined to calculate time. The `%` operator is especially useful for handling minutes and wrapping the hour around after 24 hours.
