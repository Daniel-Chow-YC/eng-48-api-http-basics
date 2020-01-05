import json

car_data = {"name": "Vauxhaul Adam", "engine": "Diesel"} # This is a dictionary

car_json_string = json.dumps(car_data) # creates a string that looks like a dictionary

# print(car_json_string)
# print(type(car_json_string))

# Creating a Json from a dictionary (encoding)
# json.dump(obj, file) --> file.json
with open('car_json_file_2.json', 'w') as jsonfile:
    json.dump(car_data, jsonfile)
# Look it created a file :)

#File.json --> Dicitonary
    # json.load(file) --> dictionary
with open('car_json_file_2.json') as jsonfile:
    car_dictionary = json.load(jsonfile)
    print(car_dictionary)
    print(type(car_dictionary))
    print(car_dictionary['name'])