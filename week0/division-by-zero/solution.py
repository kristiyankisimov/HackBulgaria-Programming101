def count_numbers(numbers):
    for number in numbers:
        smaller = []
        bigger = []
        for n in numbers:
            if n < number:
                smaller.append(number // n)
            if n > number:
                bigger.append(n // number)
            for new_number in smaller + bigger:
                if not new_number in numbers:
                    numbers.append(new_number)
    return len(numbers)