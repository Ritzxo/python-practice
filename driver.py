from calculator import Calculator

# Test case handler
test_case = input()

if test_case == "constructor_test":
    # Test calculator creation and initial state
    calc = Calculator()
    print(f"Initial result: {calc.get_result()}")
    print("Calculator created successfully")

elif test_case == "addition_test":
    # Test addition functionality
    calc = Calculator()
    result1 = calc.add(10)
    print(f"After adding 10: {result1}")
    result2 = calc.add(5)
    print(f"After adding 5: {result2}")
    print(f"Final result: {calc.get_result()}")

elif test_case == "subtraction_test":
    # Test subtraction functionality
    calc = Calculator()
    calc.add(20)  # Start with 20
    result1 = calc.subtract(8)
    print(f"After subtracting 8 from 20: {result1}")
    result2 = calc.subtract(2)
    print(f"After subtracting 2: {result2}")
    print(f"Final result: {calc.get_result()}")

elif test_case == "multiplication_test":
    # Test multiplication functionality
    calc = Calculator()
    calc.add(5)  # Start with 5
    result1 = calc.multiply(4)
    print(f"After multiplying by 4: {result1}")
    result2 = calc.multiply(2)
    print(f"After multiplying by 2: {result2}")
    print(f"Final result: {calc.get_result()}")

elif test_case == "division_test":
    # Test division functionality
    calc = Calculator()
    calc.add(100)  # Start with 100
    result1 = calc.divide(4)
    print(f"After dividing by 4: {result1}")
    result2 = calc.divide(5)
    print(f"After dividing by 5: {result2}")
    print(f"Final result: {calc.get_result()}")

elif test_case == "division_by_zero_test":
    # Test division by zero error handling
    calc = Calculator()
    calc.add(50)
    print(f"Initial value: {calc.get_result()}")
    result = calc.divide(0)  # Should print error message
    print(f"Result after division by zero: {result}")
    print(f"Value unchanged: {calc.get_result()}")

elif test_case == "clear_test":
    # Test clear functionality
    calc = Calculator()
    calc.add(25)
    calc.multiply(3)
    print(f"Before clear: {calc.get_result()}")
    result = calc.clear()
    print(f"After clear: {result}")
    print(f"Current result: {calc.get_result()}")

elif test_case == "comprehensive_test":
    # Test all operations in sequence
    calc = Calculator()
    
    # Perform a series of operations
    calc.add(10)        # result = 10
    calc.multiply(3)    # result = 30
    calc.subtract(5)    # result = 25
    calc.divide(5)      # result = 5
    
    print(f"After sequence of operations: {calc.get_result()}")
    
    # Test error handling
    calc.divide(0)      # Should print error
    print(f"After division by zero attempt: {calc.get_result()}")
    
    # Clear and start fresh
    calc.clear()
    calc.add(100)
    print(f"After clear and add 100: {calc.get_result()}")

else:
    print("Unknown test case")
