from calculator.helpers import flush_number


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

            if current_number == "" and (len(tokens) == 0 or tokens[-1] != ")"):
                return None

            current_number = flush_number(tokens, current_number)
            if current_number is None:
                return None

            # Lookahead for **
            if i + 1 < len(expression) and expression[i + 1] == "*":

                tokens.append("**")
                i += 2

            else:

                tokens.append("*")
                i += 1

        # Parentheses
        elif ch in ["(", ")"]:

            if ch == "(":

                if current_number != "":

                    current_number = flush_number(tokens, current_number)

                if current_number is None:
                    return None

                if len(tokens) > 0 and (
                    isinstance(tokens[-1], (int, float)) or tokens[-1] == ")"
                ):

                    tokens.append("*")

            if current_number != "":

                current_number = flush_number(tokens, current_number)

                if current_number is None:
                    return None

            if ch == ")" and len(tokens) > 0 and tokens[-1] == "(":
                return None

            tokens.append(ch)

            i += 1

        # Other operators
        elif ch in ["+", "-", "/", "%"]:

            # Unary minus
            if ch == "-":

                if current_number == "" and (
                    len(tokens) == 0
                    or tokens[-1] in ["+", "-", "*", "/", "%", "**", "("]
                ):

                    current_number = "-"
                    i += 1
                    continue

            # Invalid operator chaining
            if current_number == "" and (
                len(tokens) == 0 or tokens[-1] in ["+", "-", "*", "/", "%", "**", "("]
            ):
                return None

            current_number = flush_number(tokens, current_number)

            if current_number is None:
               return None
        
            tokens.append(ch)

            i += 1

    # Invalid trailing operator
    if current_number == "" and (
        len(tokens) == 0 or tokens[-1] in ["+", "-", "*", "/", "%", "**", "("]
    ):
        return None

    current_number = flush_number(tokens, current_number)

    if current_number is None:
        return None

    # Unmatched parentheses
    if tokens.count("(") != tokens.count(")"):
        return None

    return tokens
