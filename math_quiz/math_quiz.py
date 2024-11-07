import random


def random_int(min, max):
    
    # Returns a random integer within a value range of 'min' and 'max' (inclusive).
    return random.randint(min, max)


def random_math_operator():

    # Returns a random operator out of the three pre-defined ones.
    return random.choice(['+', '-', '*'])


def math_operation(num_1, num_2, operation):

    """
    Performs a mathematical operation on two numbers and returns the whole expression and result.

    Parameters:
        num_1 (int): First number in the expression.
        num_2 (int): Second number in the expression.
        operation (str): The math operation to be perform.

    Returns the mathematical expression as a string and the result as an integer.
    """

    math_expression = f"{num_1} {operation} {num_2}"

    # Mathematical operations
    if operation == '+': result = num_1 + num_2
    elif operation == '-': result = num_1 - num_2
    else: result = num_1 * num_2

    return math_expression, result

def math_quiz():

    """
    Generates three questions with random numbers and operators. The user earns a point 
    for each correct answer, and the final score is displayed at the end of the game.
    """

    point_sum = 0   # Initialize the user's score
    eq_number = 3   # Define the number of equations

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(eq_number):

        # Generate random numbers and operator for each question
        num_1 = random_int(1, 10) 
        num_2 = random_int(1, 5) 
        operator = random_math_operator()

        # Create a math problem and calculate the correct answer
        problem, answer = math_operation(num_1, num_2, operator)
        print(f"\nQuestion {i + 1}: {problem}")

        # Reqest user input and handle possible errors
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            # In case of invalid (non-integer) input
            print("Invalid input! Please answer with an integer.")
            continue  # Move to the next question without score change

        # Check if the answer is correct
        if user_answer == answer:
            print("Correct! You earned a point.")
            point_sum += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    # Display the final score
    print(f"\nGame over! Your score is: {point_sum}/{eq_number}")

if __name__ == "__main__":
    math_quiz()