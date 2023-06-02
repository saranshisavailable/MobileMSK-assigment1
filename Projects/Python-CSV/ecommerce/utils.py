def find_max(numbers):
    max = numbers[0]
    for each_number in numbers:
        if max < each_number:
            max = each_number
    return max