import re

#читаем файл
with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

#извлекаем ключевые данные
company = re.search(r"Филиал\s+(.+)", text)  #ищем строку, начинающуюся со слова "Филиал", а затем записываем найденное название компании
bin_number = re.search(r"БИН\s+(\d+)", text) #ищем строку, содержащую "БИН" и записываем номер
receipt_number = re.search(r"Чек №(\d+)", text)  #ищем строку "Чек №" и извлекаем его номер
date_time = re.search(r"Время:\s*([\d:.]+)\s*([\d.]+)", text)  #ищем строку, где указано "Время:"
total_amount = re.search(r"ИТОГО:\s*([\d\s,]+)", text)  #ищем строку "ИТОГО:"


"""
re.search(): Ищет первое совпадение, возвращает объект Match (или None)
re.findall(): Ищет все совпадения, возвращает список строк или кортежей
"""
items = re.findall(r"\d+\.\s+(.+)\n([\d,]+)\s+x\s+([\d\s,]+)\n([\d\s,]+)", text)
"""
\d+\. - номер позиции в чеке (например, "1.")
(.+) - название товара
([\d,]+) - количество товара
([\d\s,]+) - цена за единицу
([\d\s,]+) - общая сумма за товар
"""

#проходим по найденным данным и создаем словари с товарными позициями
item_list = [{"Товар": i[0].strip(), "Кол-во": i[1], "Цена": i[2].replace(" ", ""), "Сумма": i[3].replace(" ", "")} for i in items]

#вывод данных
receipt_data = {
    "Компания": company.group(1) if company else "Не найдено",
    "БИН": bin_number.group(1) if bin_number else "Не найдено",
    "Номер чека": receipt_number.group(1) if receipt_number else "Не найдено",
    "Дата и время": f"{date_time.group(2)} {date_time.group(1)}" if date_time else "Не найдено",
    "Общая сумма": total_amount.group(1).replace(" ", "") if total_amount else "Не найдено",
    "Товары": item_list
}


"""
group(1), group(2) - возвращает отдельные группы
"""

print(receipt_data)  #результат


#преобразовать в JSON
import json

with open("receipt.json", "w", encoding="utf-8") as f:
    json.dump(receipt_data, f, ensure_ascii=False, indent=4)

"""
open("receipt.json", "w", encoding="utf-8") – открывает (или создает) файл receipt.json для записи ("w")
encoding="utf-8" – используется, чтобы поддерживать русские буквы и другие символы
with open(...) as f: – автоматически закроет файл после завершения записи
json.dump(data, file) – записывает data в file в формате JSON
ensure_ascii=False – позволяет сохранить текст на русском языке (иначе "Привет" будет сохранено как "\u041f\u0440\u0438\u0432\u0435\u0442")
indent=4 – делает красивый отступ в 4 пробела, чтобы JSON-файл был читаемым
"""