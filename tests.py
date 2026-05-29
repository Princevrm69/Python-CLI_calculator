from calculator.tokenizer import parse_expression
from calculator.evaluator import evaluate_tokens
from calculator.operations import operations

test_cases = [
    "()",
    "(2+3)",
    "2+3)",
    "2++3",
    "2..5",
    "2***",
    "-",
    "10/0",

    "10%0",
    "2(3+4)",
    "(2+3)(4+5)",
    "(2+3)4",
    "2 & 3"
]


invalid_cases = [
    "()",
    "(2+3",
    "2+3)",
    "2++3",
    "2..5+1",
]


print("\n--- RUNNING TESTS ---\n")


for expr, expected in test_cases:

    parsed = parse_expression(expr)

    assert parsed is not None, f"Parsing failed for: {expr}"

    result = evaluate_tokens(parsed, operations)

    assert result == expected, f"{expr} failed " f"(expected {expected}, got {result})"

    print(f"PASS: {expr} = {result}")


print("\n--- INVALID TESTS ---\n")

for expr in invalid_cases:

    parsed = parse_expression(expr)

    assert parsed is None, f"{expr} should be invalid"

    print(f"PASS: {expr} rejected")
