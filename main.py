from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)


pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)]*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s\(]*(доб.)*[\s]*(\d+)*[\)]*'
sub = r'+7(\2)\3-\4-\5 \6\7'


def replacing_string_element(contacts_list):
    """Функция находит номера телефонов и приводит их отображение к заданному условию,
  распределяет даные по колонкам.
  """
    new_list = []
    for item in contacts_list:
        el_a = " ".join(item)
        el_b = el_a.split(" ")
        phone = re.sub(pattern, sub, item[5])
        res = [el_b[0], el_b[1], el_b[2], item[3], item[4], phone, item[6]]
        new_list.append(res)
    return new_list


def duplicate_check(new_list):
  """Функция дополняет данные из дубликатов одинаковых контактов
  """
  contacts = {}
  for items in new_list:
      if items[0] in contacts:
          item_value = contacts[items[0]]
          for i in range(len(item_value)):
              if items[i]:
                  item_value[i] = items[i]
      else:
          contacts[items[0]] = items
  return contacts.values()

if __name__== '__main__':
  a = replacing_string_element(contacts_list=contacts_list)
  b = duplicate_check(a)


  # код для записи файла в формате CSV
  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(b)
