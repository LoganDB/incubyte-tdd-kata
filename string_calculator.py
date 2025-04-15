def add(numbers):
    if not numbers:
        return 0
    delimiter=','
    if numbers.startswith('//'):
        delimiter=numbers[2]
        numbers=numbers[4:]
    nums=numbers.replace('\n',delimiter).split(delimiter)
    return sum (int(num) for num in nums)