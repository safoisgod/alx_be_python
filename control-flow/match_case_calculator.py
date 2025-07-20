def calculator(number_1, number_2, operator):
    match operator:
        case "+":
            return f"The result is {number_1 + number_2}"
        case "-":
            return f"The result is {number_1 - number_2}"
        case "*":
            return f"The result is {number_1 * number_2}"
        case "/":
            if number_2 == 0:
                return "Cannot divide by zero"
            else:
                return f"The result is {number_1 / number_2}"
        case _:
            return "unknown operator"

def receive_input():
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    operator = input("Choose the operation (+, -, *, /): ")

    print(calculator(number_1, number_2, operator))


receive_input()
