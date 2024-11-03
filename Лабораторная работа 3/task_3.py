# TODO  Напишите функцию count_letters

def count_letters(text):
    lowercase_text = text.lower()
    dictionary_number_letter = {}
    for char in lowercase_text:
        if char.isalpha():
            dictionary_number_letter[char] = dictionary_number_letter.get(char, 0) + 1
    return dictionary_number_letter

# TODO Напишите функцию calculate_frequency

def calculate_frequency(dictionary):
    total_number_letters = sum(dictionary.values())
    letter_frequency = {}
    for key, value in dictionary.items():
        letter_frequency[key] = round(value / total_number_letters, 2)
    return letter_frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
letter_count  = count_letters(main_str)
letter_frequency = calculate_frequency(letter_count)

for letter, frequency in letter_frequency.items():
    print(f"{letter}: {frequency:.2f}")
