def parse_expression(expression):

    tokens = []

    current_number = ""

    operators= ["+", "-", "*", "/", "%"]

    i = 0

    while i < len(expression):

        ch = expression[i]

        if ch == " ":
            i += 1
            continue


        if ch.isdigit() or ch == ".":

            current_number += ch
            i += 1

        elif ch == "*":

            if current_number == "" and (
                 len(tokens) == 0 or tokens[-1] != ")"
):
                 return None
            
            tokens.append(float(current_number))


            if (
                i + 1 < len(expression)
                and expression[i+1] == "*"
            ):
            
                tokens.append("**")
                i += 2

            else:
                tokens.append("*")
                i += 1
            
            current_number = ""

        
        elif ch in ["+", "-", "*", "/", "%"]:

            if ch == "-":

               if (
                   current_number == ""
                   and (
                       len(tokens) == 0
                       or tokens[-1] in ["+", "-", "*", "/", "%", "**", "("]

                   )
               ):
                   current_number = "-"
                   i += 1
                   continue         


            if current_number == "":
                return None
            

            tokens.append(float(current_number))
            tokens.append(ch)

            current_number = ""

            i += 1


        else:
            return None
            
        

    if current_number == "":
        return None
    
    tokens.append(float(current_number))

    print(tokens)

    return tokens


def evaluate_tokens(tokens, operations):

    high_precedence = ["*", "/", "%", "**"]


    i = 1
    while i < len(tokens):
        op = tokens[i]

        if op in high_precedence:

            left = tokens[i - 1]
            right = tokens[i + 1]
            
            result = operations[op](left, right)


            tokens = (
                tokens[:i - 1]
                + [result]
                + tokens[i + 2:]
            )

        
            i = 1
        else:
            i += 2


    result = tokens[0]


    for i in range(1, len(tokens), 2):

        op = tokens[i]
        num =  tokens[i + 1]

        result = operations[op](result, num)


    return result