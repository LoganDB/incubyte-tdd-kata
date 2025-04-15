def add(numbers):
    if not numbers:
        return 0
    delimiter=','
    if numbers.startswith('//'):
        delimiter=numbers[2]
        numbers=numbers[4:]
    nums=numbers.replace('\n',delimiter).split(delimiter)
    numbers_list=[int(num) for num in nums]
    negatives=[num for num in numbers_list if num < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {negatives[0]}")
    return sum (numbers_list)