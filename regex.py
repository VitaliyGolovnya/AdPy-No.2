import re

def regex_format(contacts_list):
    
    phone_pattern = re.compile(r'(8|\+7)[\s|\-]*\(?(\d{3})\)?[\s|\-]*(\d{3})[\s|\-]*(\d{2})[\s|\-]*(\d{2})(\s)?\(?(доб\.)?\s*(\d+)?\)?')
    name_pattern1 = re.compile(r'(^\w+)\s+(\w+)\s+(\w+)(,{3})(.*)')
    name_pattern2 = re.compile(r'(^\w+)\s+(\w+)(,{2})(.*)')

    for id, contact in enumerate(contacts_list):
        string = ','.join(contact)
        string = re.sub(phone_pattern, r'+7(\2)\3-\4-\5\6\7\8', string)
        string = re.sub(name_pattern1, r'\1,\2,\3,\5', string)
        string = re.sub(name_pattern2, r'\1,\2,\4', string)
        contacts_list[id] = string.split(',')
    
    return contacts_list