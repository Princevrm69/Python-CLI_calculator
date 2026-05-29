from calculator.tokenizer import parse_expression
from calculator.evaluator import evaluate_tokens
from calculator.operations import operations


# Valid expressions
test_cases = [

    ("2+3", 5.0),
    ("10-4", 6.0),
    ("2+3*4", 14.0),
    ("2++3", 5.0),
    ("(2+3)*4", 20.0),
    ("2**3**2", 512.0),
    ("2(3+4)", 14.0),
    ("(2+3)(4+5)", 45.0),
    ("(2+3)4", 20.0),
    ("((2+3)*2)+1", 11.0),

]


# Syntax / tokenizer errors
invalid_cases = [

    "()",
    "(2+3",
    "2+3)",
    "2..5",
    "2***",
    "-",
    "2 & 3",

]


# Runtime arithmetic errors
runtime_error_cases = [

    "10/0",
    "10%0",

]


print("\n--- RUNNING VALID TESTS ---\n")

for expr, expected in test_cases:

    parsed = parse_expression(expr)

    result = evaluate_tokens(
        parsed,
        operations
    )

    assert result == expected, (
        f"{expr} failed "
        f"(expected {expected}, got {result})"
    )

    print(f"PASS: {expr} = {result}")


print("\n--- RUNNING INVALID TESTS ---\n")

for expr in invalid_cases:

    try:

        parse_expression(expr)

        assert False, (
            f"{expr} should be invalid"
        )

    except ValueError:

        print(f"PASS: {expr} rejected")


print("\n--- RUNNING RUNTIME ERROR TESTS ---\n")

for expr in runtime_error_cases:

    try:

        parsed = parse_expression(expr)

        evaluate_tokens(
            parsed,
            operations
        )

        assert False, (
            f"{expr} should fail"
        )

    except ValueError:

        print(f"PASS: {expr} rejected")


print("\nALL TESTS PASSED")