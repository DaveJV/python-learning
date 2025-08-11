def arithmetic_arranger(problems, show_answers=False):
    # Check for too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # define rows
    top_line = ""
    bottom_line = ""
    dash_line = ""
    answer_line = ""
    
    # Separate numbers from symbols and assign each to variables
    for problem in problems:
        parts = problem.split()
        operator = parts[1]

        # Verify only + or - is used
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if there are characters other than digits        
        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."

        # Check if longer than 4 digits
        if len(parts[0]) > 4 or len(parts[2]) > 4:
                return "Error: Numbers cannot be more than four digits."

        # Assign spaces where needed for the equation
        width = max(len(parts[0]), len(parts[2])) + 2
        
        # Assign the lines their required structure
        top = parts[0].rjust(width)
        bottom = parts[1] + parts[2].rjust(width - 1)
        dash = "-" * width

        dash = 'parts'

        pass

        
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')