from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv",encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# print(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ

#корректное ФИО в новом списке
new_list = []
for person in contacts_list:
    person[0:3] = [' '.join(person[0:3])]
    name = person[0].split()
    name.extend(person[1:])
    new_list.append(name)
# print(new_list)

#регулярка для телефона с добавочным
import re
resub_list = []
for row in new_list:
    text = ",".join(row)
    # print(text)
    pattern = re.compile(r"(\+7|8)[\s-]*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(*\w*\.*\s*(\d+)*\)*")
    result = pattern.sub(r"+7(\2)-\3-\4-\5 (\6)",text)
    # print(result)
    new_text = result.split(",")
    resub_list.append(new_text)
print(resub_list)

#убрать дублированные имена
#вспомогат метод
# l1 = ['Лагунцов', 'Иван', 'Алексеевич', 'Минфин', '', '+7(495)-913-11-11 (0792)', '']
# l2 = ['Лагунцов', 'Иван', '',            '',      '', 'Ivan.Laguntcov@minfin.ru']

def delete(list1,list2):
    result_list = []
    for key,val in zip(list1,list2):
        if val == key and val != '':
            result_list.append(val)
        if val == key and val == '':
            result_list.append(val)
        elif val == '' and key!= '':
            result_list.append(key)
        elif key == ''and val!= '':
            result_list.append(val)
        elif val != key:
            result_list.append(key)
            result_list.append(val)
    return result_list

# delete(l1,l2)
# print(delete(l1,l2))


test_list = []
for el in resub_list:
    for el1 in resub_list:
        if el1[0] in el and el1[1] in el and el1 != el:
            test_list.append(delete(el,el1))
            resub_list.remove(el)
            resub_list.remove(el1)
for el in test_list:
    resub_list.append(el)
print(resub_list)
print(test_list)



# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(resub_list)
