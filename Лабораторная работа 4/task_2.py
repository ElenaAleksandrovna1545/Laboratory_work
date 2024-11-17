# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, "r" ,encoding="utf-8") as f:
        csv_data = [line for line in csv.DictReader(f)]

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w", encoding="utf8") as f:
        json.dump(csv_data, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
