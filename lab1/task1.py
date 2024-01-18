numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers_sum = 0
for i in numbers:
    if i != None:
        numbers_sum+=i
numbers_count = len(numbers)
for i in range(len(numbers)):
    if numbers[i] == None:
        numbers[i] = numbers_sum / numbers_count


print("Измененный список:", numbers)
