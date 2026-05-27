from operations import operations
from utils import parse_expression, evaluate_tokens


history = []


while True:

    expr = input(
        "\nEnter expression "
        "(example: 10 + 2) "
        "or command (history, clear, exit): "
    ).lower()


    if expr == "exit":
        print("Exiting calculator...")
        break


    elif expr == "history":

        if history:
            print("\nCalculation History:")

            for item in history:
                print(item)

        else:
            print("No history found")


    elif expr == "clear":
        history.clear()
        print("History cleared")


    else:

        parsed = parse_expression(expr)

        if parsed is None:
          print("Invalid expression")
          continue


        result = evaluate_tokens(parsed, operations)

        print("Result:", result)

        history.append(f"{expr} = {result}")


test_cases = [

    # Basic arithmetic
    # "2+3",
    # "10-4",
    # "6*7",
    # "8/2",

    # # Precedence
    # "2+3*4",
    # "10-2*3",
    # "100/5+2",

    # # Parentheses
    # "(2+3)*4",
    # "2*(3+4)",
    "((2+3)*2)+1",

    # Nested parentheses
#     "2*(3+(4*2))",
#     "(2+(3*(4+1)))",

#     # Unary minus
#     "-5+2",
#     "2*-3",
#     "(-5+2)*3",

#     # Exponentiation
#     "2**3",
#     "2**3+1",

#     # Invalid expressions
#     "()",
#     "(2+3",
#     "2+3)",
#     "2++3",
#     "2..5+1",
#     "2(3+4)",

 ]


print("\n--- TEST RESULTS ---\n")

for expr in test_cases:

    parsed = parse_expression(expr)

    if parsed is None:

        print(f"{expr} -> Invalid expression")
        continue


    result = evaluate_tokens(parsed, operations)

    print(f"{expr} = {result}")