from django.contrib.auth.models import User
import openai
from openai.error import RateLimitError
from .models import Articles, Config
import ast
import threading
import time
import logging


# Создаем объект логгера
logger = logging.getLogger(__name__)


def get_list_of_items(article) -> list:
    """
    Пишет список пунктов статьи по ключевым словам
    :param article_id: ID статьи
    :return: Список пунктов статьи
    """

    user = User.objects.get(id=article.user_id)
    openai.api_key = user.profile.openai_api_key

    congig = Config.objects.get(id=1)
    promt_items = congig.promt_items

    keywords = article.keywords
    messages = [{"role": "system", "content": promt_items},
                {"role": "user", "content": keywords}]

    num_retries = 2  # Количество попыток
    retries = 0

    while retries < num_retries:
        try:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',  # Используйте нужную модель
                messages=messages
            )
            response_text = response.choices[0].message['content']
            print(response_text)
            try:
                response_list = ast.literal_eval(response_text)
                print(response_list)
                if type(response_list) is list:
                    return response_list
                else:
                    return []
            except:
                return []
        except RateLimitError as e:
            print(f":Rate limit reached. Waiting for 20 seconds... ({str(e)})")
            retries += 1
            if retries < num_retries:
                time.sleep(20)
    return []


def get_item_text(article, item: str) -> str:
    congig = Config.objects.get(id=1)
    promt_article = congig.promt_article

    keywords = article.keywords
    structure = article.structure
    messages = [{"role": "system", "content": promt_article},
                {"role": "user", "content": f"""
                        Список разделов: {structure}\n\n
                        Раздел по которому нужно составаить текст: {item}\n\n
                        Ключевые слова: {keywords}
                        """}]

    num_retries = 2  # Количество попыток
    retries = 0

    while retries < num_retries:
        try:
            print(item)
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',  # Используйте нужную модель
                messages=messages
            )
            response_text = response.choices[0].message['content']

            if type(response_text) is str:
                return response_text

            return 'Ошибка'
        except RateLimitError as e:
            print(item + f": Rate limit reached. Waiting for 20 seconds... ({str(e)})")
            retries += 1
            if retries < num_retries:
                time.sleep(20)
    return 'Ошибка'


def get_article(keywords: str, user_id: int):
    article = Articles.objects.create(
        user_id=user_id,
        keywords=keywords,
        status='В работе'
    )

    # Получение содержания статьи
    list_of_items = get_list_of_items(article)

    article.structure = list_of_items
    article.save()

    # Получения пункта статьи
    for item in list_of_items:
        item_text = get_item_text(article, item)
        print(item)
        try:
            content_dict = ast.literal_eval(article.content)
            if type(content_dict) is dict:
                content_dict[item] = item_text
                article.content = str(content_dict)
                article.save()
        except Exception as e:
            content_dict = ast.literal_eval(article.content)
            content_dict[item] = 'Ошибка'
            article.content = str(content_dict)
            article.save()
    article.status = 'Готов'
    article.save()
    return


class GetArticleThread(threading.Thread):
    def __init__(self, user_id, keywords):
        self.user_id = user_id
        self.keywords = keywords
        super().__init__()

    def run(self):
        get_article(self.user_id, self.keywords)
