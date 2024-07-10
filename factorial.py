global_number = 0

def factorial(number):
  global global_number  
  global_number = number

  if number > 10:
    return "Number too large!"

  result = 1
  for i in range(2, number + 1):
    result *= i

  return result

my_num = 5
answer = factorial(my_num)
print(f"The factorial of {my_num} is {answer}")
