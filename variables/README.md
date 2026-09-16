# Miles and Kilometers Converter

## Objective

Create a Python program that converts:

* Miles to kilometers
* Kilometers to miles

The conversion is based on:

```text
1 mile ≈ 1.61 kilometers
```

## Given Values

```python
kilometers = 12.25
miles = 7.38
```

## Solution

```python
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
```

## Output

```text
7.38 miles is 11.88 kilometers
12.25 kilometers is 7.61 miles
```

## Explanation

### Miles to Kilometers

To convert miles to kilometers, multiply the number of miles by `1.61`:

```python
miles_to_kilometers = miles * 1.61
```

For `7.38` miles:

```text
7.38 × 1.61 = 11.8818
```

The `round()` function displays the result to two decimal places:

```python
round(miles_to_kilometers, 2)
```

Result:

```text
11.88
```

### Kilometers to Miles

To convert kilometers to miles, divide the number of kilometers by `1.61`:

```python
kilometers_to_miles = kilometers / 1.61
```

For `12.25` kilometers:

```text
12.25 ÷ 1.61 ≈ 7.6087
```

Rounded to two decimal places:

```text
7.61
```

## Key Concepts

* `*` is used for multiplication.
* `/` is used for division.
* Variables store values that can be used in calculations.
* `round(number, 2)` rounds a number to two decimal places.
* `print()` can display multiple arguments at once.
* Strings and variables can be combined inside `print()`.

## Conclusion

This lab demonstrates how Python can perform unit conversions using arithmetic operators, variables, and the `round()` function. The same approach can be used to create other converters, such as temperature, currency, or other units of measurement.


# Evaluating an Algebraic Expression in Python

## Objective

Complete a Python program that evaluates the following algebraic expression:

```text
3x³ - 2x² + 3x - 1
```

The calculated result must be stored in a variable named `y`.

## Solution

```python
x = 0  # Hardcode your test data here.
x = float(x)

y = 3 * x**3 - 2 * x**2 + 3 * x - 1

print("y =", y)
```

## Explanation

Python requires the multiplication operator `*` to be written explicitly.

For example:

```python
3 * x
```

represents `3x`.

Python uses `**` for powers:

```python
x**3
```

means \(x^3\), while:

```python
x**2
```

means \(x^2\).

Therefore, the complete expression:

```python
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
```

corresponds to:

```text
3x³ - 2x² + 3x - 1
```

## Testing

### Test 1 — `x = 0`

```text
y = -1.0
```

### Test 2 — `x = 1`

```text
y = 3.0
```

### Test 3 — `x = -1`

```text
y = -9.0
```

## Key Concepts

* `*` — multiplication
* `**` — exponentiation
* `-` — subtraction
* `float()` — converts a value to a floating-point number
* Variables can store calculated results.
* Python requires multiplication symbols that are often omitted in conventional algebra.

## Conclusion

This exercise demonstrates how to translate a mathematical expression into valid Python syntax. The main difference is that Python requires explicit multiplication with `*` and uses `**` for powers.
