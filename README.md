# Python CLI Calculator

A command-line calculator built in Python with a custom tokenizer and recursive expression evaluator.

Supports operator precedence, exponentiation, nested parentheses, unary negatives, and implicit multiplication.

---

## Features

- Addition, subtraction, multiplication, division, modulo
- Exponentiation (`**`)
- Operator precedence handling
- Right-associative exponentiation
- Nested parentheses
- Unary negative numbers
- Implicit multiplication
  - `2(3+4)`
  - `(2+3)(4+5)`
- Invalid expression detection
- Assertion-based automated tests

---

## Project Structure

```text
Python-CLI_calculator/
│
├── calculator/
│   ├── tokenizer.py
│   ├── evaluator.py
│   ├── operations.py
│   └── helpers.py
│
├── main.py
├── tests.py
└── README.md
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
- Handles unary negatives
- Detects invalid operator chaining
- Supports implicit multiplication
- Validates parentheses structure

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

## Automated Testing 
 
This project uses GitHub Actions to automatically run tests on every push and pull request.