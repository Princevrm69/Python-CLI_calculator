def flush_number(tokens, current_number):

    if current_number != "":

        try:
            tokens.append(float(current_number))

        except ValueError:
            return None

    return ""


def replace_section(tokens, start, end, value):

    return tokens[:start] + [value] + tokens[end:]
