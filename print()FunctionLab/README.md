Python print() Function Lab

# Scenario

This lab introduces the basic Python print() function, which is used to display text on the screen.

The goal is to experiment with Python syntax and observe what happens when the syntax is changed.

## Objectives

In this lab, you will:

- Use print() to display text.
- Print a string using double quotes.
- Print your first name.
- Observe what happens when quotation marks are removed.
- Observe what happens when parentheses are removed.
- Experiment with single and double quotation marks.
- Experiment with multiple print() functions.

## Basic Example

The first program prints:

print("Hello, Python!")


Output:

Hello, Python!


You can also use print() to display your first name:

print("YourName")


Replace YourName with your actual first name.

## Experiment 1: Removing the Quotes

Original:

print("Hello, Python!")


After removing the quotation marks:

print(Hello, Python!)


Python will produce a SyntaxError because the text is no longer written as a valid string.

Text that is meant to be printed should normally be enclosed in quotation marks.

## Experiment 2: Removing the Parentheses

Original:

print("Hello, Python!")


After removing the parentheses:

print "Hello, Python!"


In Python 3, this produces a SyntaxError because print is a function and requires parentheses.

## Experiment 3: Single Quotes

Python allows both single and double quotes for strings:

print("Hello, Python!")
print('Hello, Python!')


Both produce:

Hello, Python!
Hello, Python!

## Experiment 4: Multiple print() Functions on Different Lines
print("Hello")
print("Python!")


Output:

Hello
Python!


Each print() normally starts a new line.

## Experiment 5: Multiple print() Functions on the Same Line

You can place multiple statements on one line by separating them with semicolons:

print("Hello"); print("Python!")


Output:

Hello
Python!


Although this works, putting separate statements on separate lines is generally easier to read.

## What I Learned

This lab demonstrates that Python syntax is important. The print() function requires parentheses in Python 3, and text must be enclosed in quotation marks so Python recognizes it as a string.

I also learned that Python accepts both single and double quotation marks for strings and that multiple print() statements can be used to display multiple lines of output.

## Key Takeaways
print() displays information on the screen.
Strings should be enclosed in quotes.
Python 3 requires parentheses when calling print().
Single quotes and double quotes can both be used for strings.
Incorrect syntax can result in a SyntaxError.
