def printList(list_elem):
    if type(list_elem) == list:
        for item in list_elem:
            print(item)
    else:
        print("Error! Input must be a List")


def printDict(dict_elem):
    if type(dict_elem)== dict:
        for key in dict_elem.keys():
            print("\n ", key)
            values = ""
            for value in dict_elem[key]:
                values = values + ", " + str(value)
            print(values)
    else:
        print("Error! Input must be a dictionary")
