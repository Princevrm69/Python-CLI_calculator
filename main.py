from calculator.tokenizer import parse_expression
from calculator.evaluator import evaluate_tokens
from calculator.operations import operations

history = []


while True:

    expr = input(
        "\nEnter expression " "(example: 10 + 2) " "or command (history, clear, exit): "
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
