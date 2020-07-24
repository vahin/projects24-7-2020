def fibonacci(x):
    times = int(x)

    # first two terms
    n1, n2 = 0, 1
    i = 0

    # check if the number of terms is valid
    if times <= 0:
       print("Please enter a positive integer")
    elif times == 1:
       print("Fibonacci series:")
       print(n1)
    else:
       print("Fibonacci series:")
       while i < times:
           print(n1)
           nth = n1 + n2
           # update values
           n1 = n2
           n2 = nth
           i += 1
fibonacci(input("How many times: "))
