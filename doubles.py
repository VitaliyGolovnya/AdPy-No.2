def remove_doubles(contacts_list):
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
    return(contacts_list)