import re    #re для регулярных выражений
import json  #для того, чтобы преобразовать в этот формат


#для того чтобы загрузить XML-данные:
with open("file.xml", "r", encoding="utf-8") as file:
    xml_data = file.read()  #загрузка XML данных

def xml_file(xml):     #принимаю xml

    """
    (\w+) — имя тега.
    (.*?) — возможные атрибуты.
    (.*?) — содержимое между открывающим и закрывающим тегами.
    </\1> — закрывающий тег должен совпадать с именем открывающего тега.
    re.DOTALL позволяет работать с многострочным содержимым.
    """
    tags = re.compile(r'<(\w+)(.*?)>(.*?)</\1>', re.DOTALL)  #ищу XML-теги
    attributess = re.compile(r'(\w+)="(.*?)"')  #ищу атрибуты внутри открывающего тега
    
    def xml_element(element):

        #проверяю, содержит ли элемент XML-тег
        match = tags.search(element)
        if not match:
            return element.strip()
        
        tag, attrs, content = match.groups()   #с помощью match.groups() возвращаю (нахожу) имя тега содержимое и тд
        attributes = dict(attributess.findall(attrs))  #нахожу все атрибуты в теге и преобразует их в словарь
        
        ll = tags.findall(content)  #c помощью ll получаю список всех вложенных элементов
        if ll:
            #если вложенные элементы есть, они обрабатываются рекурсивно
            parsed_ll= [xml_element(f'<{child[0]}{child[1]}>{child[2]}</{child[0]}>') for child in ll]
            return {tag: parsed_ll if len(parsed_ll) > 1 else parsed_ll[0], **attributes}
        else:
            #если у элемента нет вложенных тегов, он преобразуется в словарь с его содержимым
            return {tag: content.strip(), **attributes} if attributes else {tag: content.strip()}
    
    return xml_element(xml)

#преобразуем в json с отступами (выбрала 5) это нужно для читаемости
json_data = json.dumps(xml_file(xml_data), indent=5)  

print(json_data) #вывод


import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("JSON Viewer")

text = scrolledtext.ScrolledText(root, width=100, height=30)
text.insert(tk.INSERT, json_data)
text.pack()

root.mainloop()
