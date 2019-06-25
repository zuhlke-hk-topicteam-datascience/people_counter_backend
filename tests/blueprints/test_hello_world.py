def test_hello_world(client):
    '''It should send correct data in HTTP response data'''
    response = client.get('/')
    assert b'Hello, World!' in response.data
