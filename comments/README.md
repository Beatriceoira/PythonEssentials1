# LAB 2.5.3 — Comments

## Objective

Improve the readability and clarity of an existing Python program by:

* Adding useful comments.
* Removing unnecessary or incorrect comments.
* Using descriptive variable names.
* Making the code easier to understand.
* Enabling code that is needed by the program.

## Original Problem

The original code contained several comments that were outdated, redundant, or misleading. It also used short variable names that did not clearly describe what the variables represented.

## Improved Code

```python
# Calculate the number of seconds in a given number of hours.

hours = 2
seconds_per_hour = 3600

print("Hours:", hours)
print("Seconds in Hours:", hours * seconds_per_hour)

print("Goodbye")
```

## Improvements Made

### 1. Descriptive Variable Names

Instead of:

```python
a = 2
seconds = 3600
```

the improved code uses:

```python
hours = 2
seconds_per_hour = 3600
```

These names make it immediately clear what each value represents.

### 2. Useful Comments

The program includes a short comment explaining its purpose:

```python
# Calculate the number of seconds in a given number of hours.
```

The comment provides useful information without explaining something that is already obvious from the code.

### 3. Removed Unnecessary Comments

Comments such as:

```python
# this program has been written two days ago
```

do not help explain how the program works, so they were removed.

### 4. Removed Incorrect Information

The original code contained a comment referring to calculating seconds for **3 hours**, while the actual value was `2` hours.

Comments should always describe the current code accurately.

### 5. Enabled the Required Calculation

The original calculation was commented out:

```python
# print("Seconds in Hours: ", a * seconds)
```

It was uncommented and updated:

```python
print("Seconds in Hours:", hours * seconds_per_hour)
```

### 6. Added the Goodbye Message

The original comments mentioned that `"Goodbye"` should be printed but that the code had not been written. The improved program actually performs the required action:

```python
print("Goodbye")
```

## Expected Output

```text
Hours: 2
Seconds in Hours: 7200
Goodbye
```

## Key Concepts

* Comments begin with `#` in Python.
* Comments should provide useful information.
* Incorrect comments can make code harder to understand.
* Descriptive variable names make code more readable.
* Comments can temporarily disable code during testing.
* Good code should be understandable even without excessive comments.

## Conclusion

This lab demonstrates that writing good Python code is not only about making a program work. **Readability and clarity are also important.** Meaningful variable names and accurate, concise comments make programs easier to understand, maintain, and debug.
