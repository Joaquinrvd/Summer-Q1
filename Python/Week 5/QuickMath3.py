# 1. Create a class called Calculator
class Calculator:
    
    # 2. Create functions for each mathematical operation: Addition, Multiplication, Division, Subtraction
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

# 3. Outside of your class definition, create an instance of your calculator class
my_calculator = Calculator()

# 4. Call each function in your calculator class and store each output into a variable. Use any values for arguments.
sum_result = my_calculator.add(10, 5)
difference_result = my_calculator.subtract(10, 5)
product_result = my_calculator.multiply(10, 5)
quotient_result = my_calculator.divide(10, 5)

# 5. Print all variables to the console
print("Addition:", sum_result)
print("Subtraction:", difference_result)
print("Multiplication:", product_result)
print("Division:", quotient_result)
