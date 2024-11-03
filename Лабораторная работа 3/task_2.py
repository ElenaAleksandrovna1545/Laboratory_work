# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=','):
    list_first_group = first_group.split(separator)
    list_second_group = second_group.split(separator)
    list_common_participants = list(set(list_first_group).intersection(set(list_second_group)))
    list_common_participants.sort()
    return list_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
participants_common = find_common_participants(participants_first_group, participants_second_group, separator='|')

print(f"Общие участники: {', '.join(participants_common)}")
