"""
Using the Python Lambda function create a Fibonacci series from 1 to 50 elements

"""

# Initialising a list with the first two Fibonacci numbers (0 and 1).
fib_list = [0, 1]

# Desired count of Fibonacci numbers
count=50


# Generating  Fibonacci sequence up to the desired count.
# We use the `map()` function with a lambda function and `any()`.
# The `map()` function applies the lambda function to each element of the range from 2 to `count`.
# The lambda function calculates the next Fibonacci number by summing the last two numbers and appends it to `fib_list`.
# `any()` is used here just to trigger the iteration over the map without needing to use the result.
any(map(lambda _: fib_list.append(sum(fib_list[-2:])),range(2, count)))



# Printing the first `count` Fibonacci numbers.
print(fib_list[:count])