from calculator.helpers import replace_section


def evaluate_tokens(tokens, operations):

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
                    return "Invalid expression"

                inner_tokens = tokens[start + 1 : i]

                # Empty parentheses
                if len(inner_tokens) == 0:
                    return "Invalid expression"

                inner_result = evaluate_tokens(inner_tokens, operations)

                if inner_result == "Invalid expression":
                    return "Invalid expression"

                tokens = replace_section(tokens, start, i + 1, inner_result)

                break

        if not found_closing:
            return "Invalid expression"

    # Unmatched parentheses
    if "(" in tokens or ")" in tokens:
        return "Invalid expression"

    # Empty expression
    if len(tokens) == 0:
        return "Invalid expression"

    # Right-associative exponentiation
    i = len(tokens) - 2

    while i >= 1:

        if tokens[i] == "**":

            left = tokens[i - 1]
            right = tokens[i + 1]

            result = operations["**"](left, right)

            tokens = replace_section(tokens, i - 1, i + 2, result)

        i -= 2

    # High precedence
    high_precedence = ["*", "/", "%"]

    i = 1

    while i < len(tokens):

        op = tokens[i]

        if op in high_precedence:

            left = tokens[i - 1]
            right = tokens[i + 1]

            result = operations[op](left, right)

            tokens = replace_section(tokens, i - 1, i + 2, result)

            i = 1

        else:
            i += 2

    # Remaining low precedence
    result = tokens[0]

    for i in range(1, len(tokens), 2):

        op = tokens[i]
        num = tokens[i + 1]

        result = operations[op](result, num)

    return result
