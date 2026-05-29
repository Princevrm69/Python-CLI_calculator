from calculator.tokenizer import parse_expression
from calculator.evaluator import evaluate_tokens
from calculator.operations import operations


print(
    "\n"
    "==================================\n"
    "      Python CLI Calculator\n"
    "==================================\n"
)

print("Type 'help' for available commands.\n")


history = []


while True:

    expr = input(
        "\nEnter expression " "(example: 10 + 2) " "or command (history, clear, exit): "
    ).lower()


    if expr == "help":

     print(
        "\nAvailable Commands:\n"
        "- help\n"
        "- history\n"
        "- clear\n"
        "- exit\n"
        "\nExamples:\n"
        "2+3\n"
        "(2+3)*4\n"
        "2(3+4)\n"
        "2**3**2\n"
    )

    if expr == "exit":
        print("Exiting calculator...")
        break

    elif expr == "history":

        if history:
            print("\nCalculation History")
            print("-------------------")

            for index, item in enumerate(history, start=1):

             print(f"{index}. {item}")

        else:
            print("No history found")

    elif expr == "clear":
        history.clear()
        print("History cleared successfully.")

    else:

        try:

            parsed = parse_expression(expr)

            result = evaluate_tokens(
                parsed,
              operations
            )

            print(f"\nResult: {result}")

            history.append(f"{expr} = {result}")

        except ValueError as e:

            print(f"\nError: {e}")