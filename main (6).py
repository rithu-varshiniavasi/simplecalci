def calculator():
  # Take two numbers as input from the user
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  # Perform the operations
  addition = num1 + num2
  subtraction = num1 - num2
  multiplication = num1 * num2
  if num2 != 0:
      division = num1 / num2
  else:
      division = "undefined (cannot divide by zero)"

  # Print the results
  print(f"{num1} + {num2} = {addition}")
  print(f"{num1} - {num2} = {subtraction}")
  print(f"{num1} * {num2} = {multiplication}")
  print(f"{num1} / {num2} = {division}")

# Run the calculator function
calculator()
