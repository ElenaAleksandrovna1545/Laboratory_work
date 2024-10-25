numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

missing_index = numbers.index(None)
length_numbers = len(numbers)
total_numbers = sum(numbers[0:4]) + sum(numbers[5:])
arithmetic_mean_numbers = total_numbers / length_numbers
numbers[missing_index] = arithmetic_mean_numbers
print("Измененный список:", numbers)
