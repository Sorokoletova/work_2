import json
from json import JSONDecodeError
from exceptions import ErrorContentException, ErrorFiletypeException

FILE_POST_DATA = "data/data.json"
FILE_COMMENT_DATA = "data/comments.json"


def get_json_loading(load_file):
    """ Получаем данные из файла"""
    try:
        with open(load_file, encoding='utf8') as file:
            data_list = json.load(file)
        return data_list
    except (FileNotFoundError, JSONDecodeError):
        raise ErrorContentException("Файл не найден или не может быть преобразован")


def get_posts_all():
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


# print(get_posts_by_user('leo'))


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста"""
    comments_list = get_json_loading(FILE_COMMENT_DATA)
    comments_user = []
    for comment in comments_list:
        if comment["post_id"] == post_id:
            comments_user.append(comment)

    return comments_user


# print(get_comments_by_post_id(1))


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    post_list = get_json_loading(FILE_POST_DATA)
    post_query = []
    for post in post_list:
        if query.lower() in post["content"].lower():
            post_query.append(post)

    return post_query


# print(search_for_posts('смотр'))


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    post_list = get_json_loading(FILE_POST_DATA)
    post_pk = None
    for post in post_list:
        if post["pk"] == pk:
            post_pk = post
            break
    return post_pk

# print(get_post_by_pk(8))
# def get_post_content(content):
#     """Получаем пост по контенту"""
#     try:
#         posts = get_posts_list()
#         content_l = content.lower()
#         post_content = []
#         for post in posts:
#             if content_l in post["content"].lower():
#                 post_content.append(post)
#         return post_content
#     except TypeError:
#         raise ErrorContentException("Не подготовлены данные для выбора")
#
#
# def add_post_pictures(picture):
#     """" Записывает картинку из поста в uploads/picture/ """
#
#     filename = picture.filename
#     file_type = filename.split('.')[-1]
#     if file_type not in ["jpeg", "jpg", "png"]:
#         raise ErrorFiletypeException
#     picture.save(f"uploads/picture/{filename}")
#
#     return f"uploads/picture/{filename}"
#
#
# def add_post_json(post):
#     """" Записывает данные поста в posts.json """
#
#     posts = get_posts_list()
#     posts.append(post)
#     try:
#         with open("posts.json", "w", encoding='utf-8') as file:
#             json.dump(posts, file, ensure_ascii=False)
#         return "Данные записаны"
#     except (FileNotFoundError, JSONDecodeError):
#         raise ErrorContentException("Файл для записи не найден или не может быть преобразован")
