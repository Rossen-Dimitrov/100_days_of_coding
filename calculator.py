from calculator_logo import logo


def add(n_1: int, n_2: int):
    """Add two numbers and return their sum"""
    return n_1 + n_2


def subtract(n_1: int, n_2: int):
    """Subtract two numbers and return difference"""
    return n_1 - n_2


def multiply(n_1: int, n_2: int):
    """Multiply two numbers and return result"""
    if n_1 == 0 or n_2 == 0:
        return f"Invalid number"
    return n_1 * n_2


def divide(n_1: int, n_2: int):
    """Divide two numbers and return result"""
    if n_1 == 0 or n_2 == 0:
        return f"Invalid number"
    return n_1 / n_2


def calculator():
    print(logo)
    num_1 = float(input("Enter number\n"))
    should_continue = True

    while should_continue:
        print("+ - * /")
        operation = input('Chose operation from list above\n')
        cur_opp = operations_dict[operation]
        num_2 = float(input("Enter number\n"))

        answer = cur_opp(num_1, num_2)
        print(f"{num_1} {operation} {num_2} = {answer}")

        if input(f'Do you continue calculating with {answer}?\n type "y" or "n" to start new calculation') == 'y':
            num_1 = answer
        else:
            should_continue = False
            calculator()


operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

calculator()




