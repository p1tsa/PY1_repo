# TODO Напишите функцию find_common_participants
def find_common_participants(string1, string2, separator=","):
    participants1 = set(string1.split(separator))
    participants2 = string2.split(separator)

    return list(participants1.intersection(participants2))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
