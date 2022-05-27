import get as a


valid_email = 'vasya@mail.com'
valid_password = '12345'

not_valid_email = 'asdkdail.com'
not_valid_password = 'kdd22k'


def test_get_api_for_valid_user(email=valid_email, password=valid_password):
    status, result = a.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_api_for_not_valid_user(email=valid_email, password=valid_password):
    status, result = a.get_api_key(email, password)
    assert status == 403


def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = a.get_api_key(valid_email, valid_password)
    status, result = a.get_api_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_get_all_pets_with_not_valid_key(filter=''):
    _, auth_key = a.get_api_key(not_valid_email, not_valid_password)
    status, result = a.get_api_pets(auth_key, filter)
    assert status == 403
    assert len(result['pets']) > 0


def test_post_create_pet_valid():
    status, result = a.post_api_create_pet('6df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6', 'Light', 'dog', 5)
    assert status == 200


def test_post_create_pet_not_valid():
    status, result = a.post_api_create_pet('df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6', 'Light', 'dog', 5)
    assert status == 403


def test_post_api_pets_set_photo_valid():
    status, result = a.post_api_pets_set_photo('6df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6', 'bfb0e44d-4a2a-4a53-afcb-347dafb9e6ca', 'photo.jpg')
    assert status == 200


def test_post_api_pets_set_photo_not_valid():
    status, result = a.post_api_pets_set_photo('df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6', 'bfb0e44d-4a2a-4a53-afcb-347dafb9e6ca', 'photo.jpg')
    assert status == 403


def test_post_api_pets_valid():
    status, result = a.post_api_pets('6df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6', 'Wolf', 'wolf', '9', 'wolf.jpg')
    assert status == 200


def test_post_api_pets_not_valid():
    status, result = a.post_api_pets('df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6', 'Wolf', 'wolf', '9', 'wolf.jpg')
    assert status == 403


def test_delete_api_pets_valid():
    status, result = a.delete_api_pets('6df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6',
                       '89b77c16-1af7-48b1-85c8-fb0af30023b7')
    assert status == 200


def test_delete_api_pets_not_valid():
    status, result = a.delete_api_pets('df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6',
                       '89b77c16-1af7-48b1-85c8-fb0af30023b7')
    assert status == 403


def test_put_api_pets_valid():
    status, result = a.put_api_pets('6df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6',
     'ec44e494-979d-43c6-931a-9f713136483f', 'Coon', 'animal', 8)
    assert status == 200


def test_put_api_pets_not_valid():
    status, result = a.put_api_pets('6df7af8769e5ae0c902e44e5f317e6379b26217f92dfc5b70091baa6',
     'ec44e494-979d-43c6-931a-9f713136483f', 'Coon', 'animal', 8)
    assert status == 403



