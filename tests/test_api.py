def test_get_post_json_all(client, keys_post):
    response = client.get('/api/posts')
    assert isinstance(response.json, list)

    for post in response.json:
        if list(post.keys()) != keys_post:
            assert False
    assert True


def test_get_post_id(client, keys_post):
    response = client.get('/api/posts/<post_id>')
    assert isinstance(response.json, list)

    for post in response.json:
        if list(post.keys()) != keys_post:
            assert False
    assert True