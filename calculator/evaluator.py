from calculator.helpers import replace_section


def evaluate_tokens(tokens, operations):

    # Empty expression
    if len(tokens) == 0:
        raise ValueError("Empty token sequence")

    # Recursive parentheses evaluation
    while "(" in tokens:

        start = None
        found_closing = False

        for i in range(len(tokens)):

            if tokens[i] == "(":

                start = i

            elif tokens[i] == ")":

                found_closing = True

                if start is None:
                    raise ValueError(
                        "Unexpected closing parenthesis"
                    )

                inner_tokens = tokens[start + 1 : i]

                if len(inner_tokens) == 0:
                    raise ValueError(
                        "Empty parentheses detected"
                    )

                inner_result = evaluate_tokens(
                    inner_tokens,
                    operations
                )

                tokens = replace_section(
                    tokens,
                    start,
                    i + 1,
                    inner_result
                )

                break

        if not found_closing:
            raise ValueError(
                "Unmatched parentheses"
            )

    # Safety check
    if "(" in tokens or ")" in tokens:
        raise ValueError(
            "Unmatched parentheses"
        )

    # Right-associative exponentiation
    i = len(tokens) - 2

    while i >= 1:

        if tokens[i] == "**":

            if i - 1 < 0 or i + 1 >= len(tokens):
                raise ValueError(
                    "Incomplete exponent expression"
                )

            left = tokens[i - 1]
            right = tokens[i + 1]

            result = operations["**"](
                left,
                right
            )

            tokens = replace_section(
                tokens,
                i - 1,
                i + 2,
                result
            )

        i -= 2

    # High precedence
    high_precedence = ["*", "/", "%"]

    i = 1

    while i < len(tokens):

        op = tokens[i]

        if op in high_precedence:

            if i - 1 < 0 or i + 1 >= len(tokens):
                raise ValueError(
                    "Incomplete expression"
                )

            left = tokens[i - 1]
            right = tokens[i + 1]

            if op not in operations:
                raise ValueError(
                    f"Unknown operator '{op}'"
                )

            result = operations[op](
                left,
                right
            )

            tokens = replace_section(
                tokens,
                i - 1,
                i + 2,
                result
            )

            i = 1

        else:
            i += 2

    # Remaining low precedence
    result = tokens[0]

    for i in range(1, len(tokens), 2):

        if i + 1 >= len(tokens):
            raise ValueError(
                "Incomplete expression"
            )

        op = tokens[i]
        num = tokens[i + 1]

        if op not in operations:
            raise ValueError(
                f"Unknown operator '{op}'"
            )

        result = operations[op](
            result,
            num
        )

    return result