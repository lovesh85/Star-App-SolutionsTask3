class DivisionCalculator:
    def __init__(self):
        self.numerator = None
        self.denominator = None

    def get_input(self):
        while True:
            try:
                self.numerator = float(input("Enter the numerator: "))  
                self.denominator = float(input("Enter the denominator: "))
                break  
            except ValueError:
                print("Invalid input! Please enter numbers only.\n")  
    def divide(self):
        try:
            result = self.numerator / self.denominator 
            return f" Result: {result}"
        except ZeroDivisionError:
            return " Error: Cannot divide by zero!"
        except Exception as e:
            return f" Unexpected error: {e}"  

calculator = DivisionCalculator()
calculator.get_input()
print(calculator.divide())
