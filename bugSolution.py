def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # Or handle it appropriately, e.g., raise an exception, return a special value, etc.

result = my_function(10, 0) 
print(result) # Output: 0