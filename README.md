i# alx_be_python

## fns_and_dsa

### arithmetic_operations.py

This script defines a function `perform_operation` that performs basic arithmetic operations.

#### Function Definition

##### `perform_operation(num1, num2, operation)`

- **Parameters:**
  - `num1` (float): The first number.
  - `num2` (float): The second number.
  - `operation` (string): The operation to perform. Acceptable values are 'add', 'subtract', 'multiply', 'divide'.

- **Returns:**
  - The result of the arithmetic operation.
  - For division, if `num2` is 0, it returns `"Error: Division by zero"`.
  - If an invalid operation is provided, it returns `"Error: Invalid operation"`.

#### Usage

To test the function, use the provided `main.py` script:

```python
from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

