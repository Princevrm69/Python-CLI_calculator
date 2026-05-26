def flush_number(tokens, current_number):

    if current_number != "":
        tokens.append(float(current_number))

    return ""



def replace_section(tokens, start, end, value):

    return (
        tokens[:start]
        + [value]
        + tokens[end:]
    )



def parse_expression(expression):

    tokens = []

    current_number = ""

    i = 0


    while i < len(expression):

        ch = expression[i]


        # Ignore spaces
        if ch == " ":
            i += 1
            continue


        # Build numbers
        if ch.isdigit() or ch == ".":

            current_number += ch
            i += 1


        # Handle * and **
        elif ch == "*":

            if current_number == "" and (
                len(tokens) == 0
                or tokens[-1] != ")"
            ):
                return None


            current_number = flush_number(
                tokens,
                current_number
            )


            # Lookahead for **
            if (
                i + 1 < len(expression)
                and expression[i + 1] == "*"
            ):

                tokens.append("**")
                i += 2

            else:

                tokens.append("*")
                i += 1


        # Parentheses
        elif ch in ["(", ")"]:


            # Flush before closing parenthesis
            if current_number != "":

                current_number = flush_number(
                    tokens,
                    current_number
                )


            # Validation for opening parenthesis
            if ch == "(":

                # Reject implicit multiplication
                if (
                    len(tokens) > 0
                    and (
                        isinstance(tokens[-1], float)
                        or tokens[-1] == ")"
                    )
                ):
                    return None


            # Validation for closing parenthesis
            if ch == ")":

                if (
                    len(tokens) == 0
                    or tokens[-1] in [
                        "+", "-", "*",
                        "/", "%", "**", "("
                    ]
                ):
                    return None


            tokens.append(ch)

            i += 1


        # Other operators
        elif ch in ["+", "-", "/", "%"]:


            # Unary minus
            if ch == "-":

                if (
                    current_number == ""
                    and (
                        len(tokens) == 0
                        or tokens[-1] in [
                            "+", "-", "*",
                            "/", "%", "**", "("
                        ]
                    )
                ):

                    current_number = "-"
                    i += 1
                    continue


            # Invalid operator placement
            if current_number == "":
                return None


            current_number = flush_number(
                tokens,
                current_number
            )

            tokens.append(ch)

            i += 1


        else:
            return None


    # Invalid trailing operator
    if current_number == "":

        if (
            len(tokens) == 0
            or tokens[-1] in [
                "+", "-", "*",
                "/", "%", "**", "("
            ]
        ):
            return None


    current_number = flush_number(
        tokens,
        current_number
    )


    return tokens



def evaluate_tokens(tokens, operations):


    # Recursive parentheses evaluation
    while "(" in tokens:

        start = None


        for i in range(len(tokens)):

            if tokens[i] == "(":

                start = i


            elif tokens[i] == ")":


                if start is None:
                    return "Invalid expression"


                inner_tokens = tokens[start + 1:i]


                # Empty parentheses
                if len(inner_tokens) == 0:
                    return "Invalid expression"


                inner_result = evaluate_tokens(
                    inner_tokens,
                    operations
                )


                if inner_result == "Invalid expression":
                    return "Invalid expression"


                tokens = replace_section(
                    tokens,
                    start,
                    i + 1,
                    inner_result
                )

                break


    # Unmatched parentheses
    if "(" in tokens or ")" in tokens:
        return "Invalid expression"


    # Empty expression
    if len(tokens) == 0:
        return "Invalid expression"


    # High precedence
    high_precedence = ["*", "/", "%", "**"]


    i = 1

    while i < len(tokens):

        op = tokens[i]


        if op in high_precedence:

            left = tokens[i - 1]
            right = tokens[i + 1]


            result = operations[op](left, right)


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

        op = tokens[i]
        num = tokens[i + 1]

        result = operations[op](result, num)


    return result