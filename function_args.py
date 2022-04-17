def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(f"Total = {add_numbers(1, 3, 5, 7, 9)}")