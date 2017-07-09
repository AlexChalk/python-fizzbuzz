def fizzbuzz(n):
    if n % 15 == 0:
        return "Fizzbuzz"
    elif n % 5 == 0:
        return "buzz"
    elif n % 3 == 0:
        return "fizz"
    else:
        return n

def fizzbuzz_loop():
    result = []
    for num in range(1,31):
        result.append(fizzbuzz(num))
    return result
