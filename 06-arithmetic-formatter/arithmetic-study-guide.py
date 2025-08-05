def arithmetic_arranger(problems, show_answers=False):
    # Step 1A: Validate number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize rows
    top_row = ""
    bottom_row = ""
    dashes_row = ""
    answers_row = ""

    for i, problem in enumerate(problems):
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Invalid problem format."

        operand1, operator, operand2 = parts

        # Step 1B: Check valid operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Step 1C: Check if both operands are digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Step 1D: Check operand length
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Step 2: Compute width of formatting
        width = max(len(operand1), len(operand2)) + 2

        # Step 3: Format lines
        top = operand1.rjust(width)
        bottom = operator + operand2.rjust(width - 1)
        dash = '-' * width
        answer = str(eval(problem)).rjust(width)

        # Step 4: Add spacing (4 spaces between problems, but not after last)
        if i > 0:
            top_row += "    "
            bottom_row += "    "
            dashes_row += "    "
            answers_row += "    "

        top_row += top
        bottom_row += bottom
        dashes_row += dash
        answers_row += answer

    # Step 5: Combine and return
    arranged = top_row + "\n" + bottom_row + "\n" + dashes_row
    if show_answers:
        arranged += "\n" + answers_row

    return arranged
