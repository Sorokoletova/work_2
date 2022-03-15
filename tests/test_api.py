def test_get_post_json_all(client, keys_post):
    response = client.get('/api/posts')
    assert isinstance(response.json, list)

    for post in response.json:
        if set(post.keys()) != set(keys_post):
            assert False



def test_get_post_id(client, keys_post):
    response = client.get('/api/posts/1')
    assert isinstance(response.json, dict)
    if set(response.json.keys()) != set(keys_post):
            assert False

