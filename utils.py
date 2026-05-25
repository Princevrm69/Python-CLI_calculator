def parse_expression(expression):

    parts = expression.split()

    if len(parts) < 3:
        return None

    if len(parts) % 2 == 0:
        return None


    tokens = []


    for i in range(len(parts)):


        if i % 2 == 0:

            try:
                tokens.append(float(parts[i]))

            except ValueError:
                return None


        else:
            tokens.append(parts[i])


    return tokens



def evaluate_tokens(tokens, operations):

    result = tokens[0]


    for i in range(1, len(tokens), 2):

        op = tokens[i]
        num = tokens[i + 1]


        if op not in operations:
            return "Invalid operator"


        result = operations[op](result, num)


    return result