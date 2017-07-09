def fizzbuzz(n):
    if n % 15 == 0:
        return "Fizzbuzz"
    elif n % 5 == 0:
        return "buzz"
    elif n % 3 == 0:
        return "fizz"
    else:
        return n
