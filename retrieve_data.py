import requests

url = 'http://api.postcodes.io/postcodes/'
arg = 'w139dq'

post_code = requests.get(url + arg)
dict_response = post_code.json()

# print(dict_response['result']['longitude'])
# print(dict_response['result']['latitude'])
# print(dict_response['result']['nuts'])
# print(dict_response['result']['admin_ward'])


def return_lat(p_code):
    path_url = 'http://api.postcodes.io/postcodes/'
    dictionary = requests.get(path_url + p_code).json()
    lat = dictionary['result']['latitude']
    return lat


def return_long(p_code):
    path_url = 'http://api.postcodes.io/postcodes/'
    dictionary = requests.get(path_url + p_code).json()
    long = dictionary['result']['longitude']
    return long


def data_to_txt(p_code):
    path_url = 'http://api.postcodes.io/postcodes/'
    dictionary = requests.get(path_url + p_code).json()
    lat = dictionary['result']['latitude']
    long = dictionary['result']['longitude']
    nuts = dictionary['result']['nuts']
    admin_ward = dictionary['result']['admin_ward']
    with open(f"{p_code}.txt", 'w+') as file_to_create:
        file_to_create.write(f"postcode: {p_code} \n"
                             f"latitude: {lat} \n"
                             f"longitude: {long}\n"
                             f"nuts: {nuts}\n"
                             f"admin ward: {admin_ward}")


data_to_txt('UB12XJ')
