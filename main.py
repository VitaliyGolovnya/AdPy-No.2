import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

phone_pattern = re.compile(r'(8|\+7)[\s|\-]*\(?(\d{3})\)?[\s|\-]*(\d{3})[\s|\-]*(\d{2})[\s|\-]*(\d{2})(\s)?\(?(доб\.)?\s*(\d+)?\)?')
name_pattern1 = re.compile(r'(^\w+)\s+(\w+)\s+(\w+)(,{3})(.*)')
name_pattern2 = re.compile(r'(^\w+)\s+(\w+)(,{2})(.*)')

for id, contact in enumerate(contacts_list):
    string = ','.join(contact)
    string = re.sub(phone_pattern, r'+7(\2)\3-\4-\5\6\7\8', string)
    string = re.sub(name_pattern1, r'\1,\2,\3,\5', string)
    string = re.sub(name_pattern2, r'\1,\2,\4', string)
    contacts_list[id] = string.split(',')

contact_id = {}
for id, contact in enumerate(contacts_list):
    full_name = contact[0] + contact[1]
    if full_name not in contact_id.keys():
        contact_id[full_name] = id
    else:
        for index, original_value in enumerate(contacts_list[contact_id[full_name]]):
            if original_value == "":
                contacts_list[contact_id[full_name]][index] = contact[index]
        contacts_list.pop(id)

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)