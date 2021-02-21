def AreNumbersEven(numbers):
    return [True if abs(num) % 2 == 0 else False for num in numbers]

numbers = raw_input()
integer_list = [int(i) for i in numbers.split(' ')]
even_odd_boolean_list = AreNumbersEven(integer_list)
print even_odd_boolean_list
