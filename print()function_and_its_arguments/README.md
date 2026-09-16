# LAB 2.1.12 — The `print()` Function and Its Arguments

## Objective

Practice using the `sep` and `end` keyword arguments of Python's `print()` function.

## Given Code

```python
print("Programming", "Essentials", "in")
print("Python")
```

## Solution

```python
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")
```

## Output

```text
Programming***Essentials***in...Python
```

## Explanation

* `sep="***"` specifies the separator placed between the arguments of `print()`.
* `end="..."` specifies what is printed at the end instead of the default newline.
* Because `end="..."` is used, the second `print()` continues on the same line.

## Key Concepts

### `sep`

The `sep` argument controls how multiple values are separated.

```python
print("A", "B", "C", sep="-")
```

Output:

```text
A-B-C
```

### `end`

The `end` argument controls what is printed after the `print()` statement.

```python
print("Hello", end="...")
print("World")
```

Output:

```text
Hello...World
```

## Result

The lab demonstrates how `sep` and `end` can be used to control the formatting of output in Python.


# LAB 2.1.13 — Formatting the Arrow

## Objective

Practice Python strings, escape sequences, string multiplication, quotation marks, parentheses, and case sensitivity.

## Original Code

```python
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
```

## Modified Code

### 1. Minimize `print()` invocations using `\n`

```python
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")
```

The `\n` escape sequence creates a new line inside the string, allowing multiple lines to be printed with one `print()`.

### 2. Make the arrow twice as large

```python
print("        **")
print("       ** **")
print("      **   **")
print("     **     **")
print("******     ******")
print("      **   **")
print("      **   **")
print("      *******")
```

The arrow is enlarged while maintaining its general proportions.

### 3. Duplicate the arrow side by side

A convenient way is to multiply each row by `2`:

```python
print("    *     *")
print("   * *   * *")
print("  *   * *   *")
print(" *     *     *")
print("***   *****   ***")
print("  *   * *   *")
print("  *   * *   *")
print("  ***** *****")
```

String multiplication can also be used directly:

```python
print(("    *") * 2)
```

This repeats the string, producing:

```text
    *    *
```

## Experiments and Observations

### Removing quotation marks

Strings need quotation marks.

```python
print(    *)
```

This produces a syntax error because Python no longer interprets `*` as part of a string.

Interestingly, Python may highlight a location **after** the actual mistake. This happens because Python's parser only discovers that something is wrong when it reaches a point where the code can no longer be interpreted correctly.

### Removing parentheses

The `print()` function requires parentheses in modern Python.

```python
print "Hello"
```

This results in a syntax error in Python 3.

### Changing the case of `print`

Python is **case-sensitive**.

```python
Print("Hello")
```

This does not mean the same thing as:

```python
print("Hello")
```

`Print` is treated as a different name, and unless it has been defined, Python raises a `NameError`.

### Replacing quotes with apostrophes

Single quotes can be used instead of double quotes:

```python
print('    *')
```

This works because Python accepts both single-quoted and double-quoted strings.

For example:

```python
print("Hello")
print('Hello')
```

Both produce:

```text
Hello
```

## Key Lessons

* `\n` creates a new line inside a string.
* Strings can be multiplied using `*`.
* Python requires correct syntax for function calls and strings.
* Python is case-sensitive.
* Both `'single quotes'` and `"double quotes"` can define strings.
* A syntax error may be reported at a location after the actual mistake.
* Experimenting with code is a useful way to understand how Python behaves.

## Conclusion

This exercise demonstrates that Python's output can be controlled using strings and escape sequences. It also shows how small syntax changes—such as removing quotes, parentheses, or changing capitalization—can change how Python interprets the program.
