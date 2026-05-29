from calculator.helpers import flush_number


def parse_expression(expression):

    if expression.strip() == "":
        raise ValueError("Empty expression")

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

            # Missing operator between numbers
            if (
                current_number == ""
                and len(tokens) > 0
                and isinstance(tokens[-1], (int, float))
            ):
                raise ValueError(
                    "Missing operator between numbers"
                )

            # Implicit multiplication after ')'
            if (
                current_number == ""
                and len(tokens) > 0
                and tokens[-1] == ")"
            ):
                tokens.append("*")

            current_number += ch
            i += 1

        # Handle * and **
        elif ch == "*":

          # Invalid ***
            if (
             i + 2 < len(expression)
             and expression[i] == "*"
             and expression[i + 1] == "*"
             and expression[i + 2] == "*"
        ):
             raise ValueError(
                "Invalid exponent syntax"
          )

            if current_number == "" and (
                len(tokens) == 0
                or tokens[-1] != ")"
            ):
                raise ValueError(
                    "Unexpected operator '*'"
                )

            current_number = flush_number(
                tokens,
                current_number
            )

            if current_number is None:
                raise ValueError(
                    "Invalid number format"
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

            if ch == "(":

                if current_number != "":

                    current_number = flush_number(
                        tokens,
                        current_number
                    )

                if current_number is None:
                    raise ValueError(
                        "Invalid number format"
                    )

                # Implicit multiplication
                if (
                    len(tokens) > 0
                    and (
                        isinstance(tokens[-1], (int, float))
                        or tokens[-1] == ")"
                    )
                ):

                    tokens.append("*")

            if current_number != "":

                current_number = flush_number(
                    tokens,
                    current_number
                )

                if current_number is None:
                    raise ValueError(
                        "Invalid number format"
                    )

            # Empty parentheses
            if (
                ch == ")"
                and len(tokens) > 0
                and tokens[-1] == "("
            ):
                raise ValueError(
                    "Empty parentheses detected"
                )

            # Unexpected closing parenthesis
            if (
                ch == ")"
                and tokens.count("(")
                < tokens.count(")") + 1
            ):
                raise ValueError(
                    "Unexpected closing parenthesis"
                )

            tokens.append(ch)

            i += 1

        # Other operators
        elif ch in ["+", "-", "/", "%"]:

            # Unary minus / plus
            if ch in ["-", "+"]:

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

                    current_number = ch
                    i += 1
                    continue

            # Invalid operator chaining
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
                raise ValueError(
                    f"Unexpected operator '{ch}'"
                )

            current_number = flush_number(
                tokens,
                current_number
            )

            if current_number is None:
                raise ValueError(
                    "Invalid number format"
                )

            tokens.append(ch)

            i += 1

        else:

            raise ValueError(
                f"Invalid character '{ch}'"
            )

    # Missing number after unary minus
    if current_number == "-":
        raise ValueError(
            "Missing number after unary minus"
        )

    # Invalid trailing operator
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
        raise ValueError(
            "Expression cannot end with operator"
        )

    current_number = flush_number(
        tokens,
        current_number
    )

    if current_number is None:
        raise ValueError(
            "Invalid number format"
        )

    # Unmatched parentheses
    if tokens.count("(") != tokens.count(")"):
        raise ValueError(
            "Unmatched parentheses"
        )

    return tokens