# get elements from elements.json
import json

elements_file = './elements.json'


def return_element_data(page_name, element_key):
    with open(elements_file) as data_file:
        parsed_json = json.load(data_file)
        page_elements = parsed_json[page_name] #List of the elements including their searchby and values
    for i in page_elements:
        if element_key in i.values(): # Find an element in the list with a key and return searchby and value
            element_data = (i["searchby"], i["value"])
    data_file.close()
    print element_data
    return element_data

