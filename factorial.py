# Unnecessary global variable
global_number = 0

def factorial(number):
  """Calculates the factorial of a number (badly)"""
  global global_number  # Using global variable inside function
  global_number = number

  # Hardcoded limit (not flexible)
  if number > 10:
    return "Number too large!"

  # Inefficient loop (can be recursive)
  result = 1
  for i in range(2, number + 1):
    result *= i

  return result

# Usage with bad variable naming
my_num = 5
answer = factorial(my_num)
print(f"The factorial of {my_num} is {answer}")
