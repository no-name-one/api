import requests
import json

from requests_toolbelt.multipart.encoder import MultipartEncoder


' 🍀 1 🍀 😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶'


def get_api_key(email: str, passwd: str):
    headers = {'email': email, 'password': passwd, }
    res = requests.get('https://petfriends1.herokuapp.com/api/key', headers=headers)
    status = res.status_code
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError: result = res.text
    return status, result


'-------------------------------------------------------------------------------------------------'
print(get_api_key('vasya@mail.com', '12345'))
'-------------------------------------------------------------------------------------------------'

' 🍀 2 🍀 😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶'


def get_api_pets(auth_key: str, fil: str):
    headers = {'auth_key': auth_key}
    filter = {'filter': fil}
    res = requests.get('https://petfriends1.herokuapp.com/api/pets', headers=headers, params=filter)
    status = res.status_code
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError: result = res.text
    return status, result


'-------------------------------------------------------------------------------------------------'
# print(get_api_pets('6df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6', 'my_pets'))
'-------------------------------------------------------------------------------------------------'

' 🍀 3 🍀 😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶'


def post_api_create_pet(auth_key: str, name: str, animal_type: str, age: int):
    headers = {'auth_key': auth_key}
    data = fields = {'name': name, 'animal_type': animal_type, 'age': age}
    res = requests.post('https://petfriends1.herokuapp.com/api/create_pet_simple', headers=headers, data=data)
    status = res.status_code
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError: result = res.text
    return status, result


'-------------------------------------------------------------------------------------------------'
# print(post_api_create_pet('6df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6', 'Light', 'dog', 5))
'-------------------------------------------------------------------------------------------------'

' 🍀 4 🍀 😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶'


def post_api_pets_set_photo(auth_key: str, pet_id: str, pet_photo: str):
    data = MultipartEncoder(
        fields={'pet_id': pet_id,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}
    )
    headers = {'auth_key': auth_key, 'Content-Type': data.content_type}
    res = requests.post(f'https://petfriends1.herokuapp.com/api/pets/set_photo/{pet_id}', headers=headers, data=data)
    status = res.status_code
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError: result = res.text
    return status, result


'-------------------------------------------------------------------------------------------------'
# print(post_api_pets_set_photo('6df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6',
#                               'bfb0e44d-4a2a-4a53-afcb-347dafb9e6ca', 'photo.jpg'))
'-------------------------------------------------------------------------------------------------'

' 🍀 5 🍀 😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶'


def post_api_pets(auth_key: str, name: str, animal_type: str, age: str, pet_photo: str):
    data = MultipartEncoder(
        fields={'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}
    )
    headers = {'auth_key': auth_key, 'Content-Type': data.content_type}
    res = requests.post(f'https://petfriends1.herokuapp.com/api/pets', headers=headers, data=data)
    status = res.status_code
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError: result = res.text
    return status, result


'-------------------------------------------------------------------------------------------------'
# print(post_api_pets('6df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6', 'Wolf', 'wolf', '9', 'wolf.jpg'))
'-------------------------------------------------------------------------------------------------'

' 🍀 6 🍀 😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶'


def delete_api_pets(auth_key: str, pet_id: str):
    headers = {'auth_key': auth_key,
            'pet_id': pet_id}
    res = requests.delete(f'https://petfriends1.herokuapp.com/api/pets/{pet_id}', headers=headers)
    status = res.status_code
    return status


'-------------------------------------------------------------------------------------------------'
# print(delete_api_pets('6df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6',
#                       '89b77c16-1af7-48b1-85c8-fb0af30023b7'))
'-------------------------------------------------------------------------------------------------'

' 🍀 7 🍀 😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶😶'


def put_api_pets(auth_key: str, pet_id: str, name: str, animal_type: str, age: int):
    data = {'name': name,
            'animal_type': animal_type,
            'age': age}
    headers = {'auth_key': auth_key}
    res = requests.put(f'https://petfriends1.herokuapp.com/api/pets/{pet_id}', headers=headers, data=data)
    status = res.status_code
    result = ''
    try:
        result = res.json()
    except Exception:
        json.decoder.JSONDecodeError: result = res.text
    return status, result


'-------------------------------------------------------------------------------------------------'
# print(put_api_pets('6df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6',
# 'ec44e494-979d-43c6-931a-9f713136483f', 'Coon', 'animal', 8))
'-------------------------------------------------------------------------------------------------'
