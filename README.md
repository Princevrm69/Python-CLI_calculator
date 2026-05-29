# Python CLI Calculator

A command-line calculator built in Python with a custom tokenizer and recursive expression evaluator.

Supports operator precedence, exponentiation, nested parentheses, unary operators, implicit multiplication, custom error handling, and automated testing.

---

## Features

* Addition, subtraction, multiplication, division, and modulo
* Exponentiation (`**`)
* Operator precedence handling
* Right-associative exponentiation
* Nested parentheses
* Unary negative and unary positive numbers
* Implicit multiplication

  * `2(3+4)`
  * `(2+3)(4+5)`
  * `(2+3)4`
* Custom error handling

  * Invalid operators
  * Invalid number formats
  * Unmatched parentheses
  * Division by zero
  * Modulo by zero
* Automated test suite
* GitHub Actions CI

---

## Project Structure

```text
Python-CLI_calculator/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── calculator/
│   ├── tokenizer.py
│   ├── evaluator.py
│   ├── operations.py
│   └── helpers.py
│
├── main.py
├── tests.py
├── README.md
└── .gitignore
```

---

## How It Works

### Tokenization

The tokenizer converts raw expressions into structured tokens.

Example:

```python
2(3+4)
```

becomes:

```python
[2.0, "*", "(", 3.0, "+", 4.0, ")"]
```

The tokenizer also:

* Handles unary operators
* Detects invalid operator chaining
* Supports implicit multiplication
* Validates number formats
* Validates parentheses structure

---

### Recursive Evaluation

Parentheses are evaluated recursively from the innermost expression outward.

Example:

```python
((2+3)*2)+1
```

Evaluation flow:

1. Evaluate `(2+3)`
2. Replace with `5`
3. Evaluate `(5*2)`
4. Replace with `10`
5. Compute `10+1`

---

### Exponentiation Associativity

Exponentiation is evaluated right-to-left.

Example:

```python
2**3**2
```

evaluates as:

```python
2**(3**2)
```

Result:

```python
512
```

---

## Error Handling

The calculator provides descriptive error messages for common syntax and runtime issues.

Examples:

```text
Error: Empty expression
Error: Unexpected operator '+'
Error: Invalid number format
Error: Division by zero
Error: Unmatched parentheses
```

---

## Run Calculator

```bash
python main.py
```

---

## Run Tests

```bash
python tests.py
```

---

## Example

```text
Enter expression: 2(3+4)

Result: 14.0
```

---

## Automated Testing

This project uses GitHub Actions to automatically run tests on every push and pull request.

---

## Future Improvements

* Abstract Syntax Tree (AST) parser
* Variables and assignments
* Built-in mathematical functions
* Memory registers
* Expression tree visualization
* Interactive command history

```
```
