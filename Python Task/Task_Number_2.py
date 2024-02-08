# Name : Abdul Ahad
# Roll Number : 31247
# Email : aabdulahad142@gmail.com

# make function  
def add(x, y):
      return x + y, '+'

def subtract(x, y):
  return x - y, '-'

def multiply(x, y):
  return x * y, '*'

def divide(x, y):
  if y == 0:
    return "Error: Cannot divide by zero.", '/'
  return x / y, '/'

def percentage(x, y):
  return (x * y) / 100, '%'

while True:
  print("Select operation:")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Percentage")
  print("6. Exit")

  choice = input("Enter choice (1-6): ")

  if choice == '6':
      
    print("Exiting the calculator. Goodbye!")
    
    #for exiting in calculator
    break
     
    #choice not in opreration
  if choice not in ['1', '2', '3', '4', '5']:
    print("Invalid input. Please enter a valid option.")
    continue

    #error handling
  try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
  except ValueError:
    print("Invalid input. Please enter valid numbers.")
    continue

  result, symbol = None, None
  if choice == '1':
    result, symbol = add(num1, num2)
  elif choice == '2':
    result, symbol = subtract(num1, num2)
  elif choice == '3':
    result, symbol = multiply(num1, num2)
  elif choice == '4':
    result, symbol = divide(num1, num2)
  elif choice == '5':
    result, symbol = percentage(num1, num2)

  #out put result
  print(f"Result: {num1} {symbol} {num2} = {result}")
