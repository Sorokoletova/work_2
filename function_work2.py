import json

FILE_POST_DATA = "data/data.json"
FILE_COMMENT_DATA = "data/comments.json"


def get_json_loading(load_file):
    """ Получаем данные из файла"""
    with open(load_file, encoding='utf8') as file:
        data_list = json.load(file)
        return data_list


def get_posts_all():
    """ Получаем список постов из файла"""
    posts_all = get_json_loading(FILE_POST_DATA)
    return posts_all


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя"""
    post_list = get_json_loading(FILE_POST_DATA)
    post_user = []
    for post in post_list:
        if post["poster_name"] == user_name:
            post_user.append(post)

    return post_user


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста"""
    comments_list = get_json_loading(FILE_COMMENT_DATA)
    comments_user = []
    for comment in comments_list:
        if comment["post_id"] == int(post_id):
            comments_user.append(comment)

    return comments_user


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    post_list = get_json_loading(FILE_POST_DATA)
    post_query = []
    for post in post_list:
        if query.lower() in post["content"].lower():
            post_query.append(post)

    return post_query


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    post_list = get_json_loading(FILE_POST_DATA)
    post_pk = None
    for post in post_list:
        if post['pk'] == int(pk):
            post_pk = post

    return post_pk
