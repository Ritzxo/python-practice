class Calculator:
    def __init__(self):
        # TODO: Initialize the result attribute to 0
        self.result = 0
        pass
        
    def add(self, number):
        # TODO: Add the number to result and return the new result
        self.result += number
        return self.result
        pass
    
    def subtract(self, number):
        # TODO: Subtract the number from result and return the new result
        self.result -= number
        return self.result
        pass
    
    def multiply(self, number):
        # TODO: Multiply result by the number and return the new result
        self.result *= number
        return self.result
        pass
    
    def divide(self, number):
        # TODO:
        # Check if number is 0
        if number == 0:
            print("Error: Division by zero")
            return self.result
        else:
            self.result /= number
            return self.result
        # If it is, print error message and return unchanged result
        # Otherwise, divide result by the number and return the new result
        pass
    
    def clear(self):
        # TODO: Reset result to 0 and return it
        self.result = 0
        return self.result
        pass
    
    def get_result(self):
        # TODO: Return the current value of result
        return self.result


        pass