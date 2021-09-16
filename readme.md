# Демонстрационный стенд 1

Фото блог, который показывает работу простого приложения с фронтом и бэком

## Использовалось
- Python 3.9
- Flask
- SQLite3


## Как запустить
```bash
# Перед запуском (только единожды)
export FLASK_APP=run
pip install -r requirements.txt
flask db upgrade

# Запуск
flask run

# Справка по командам
flask --help

## добавлены команды 
# flask post
# flask comments
```
## Эндпоинты

### Возвращает все посты
> GET /posts/

### Поставить лайк
> POST /posts/<<int:post_id>>/like/

### Поставить дизлайк
>POST /posts/<<int:post_id>>/dislike/"


### Возвращает все комментарии к посту
> GET /posts/<<int:post_id>>/comments/

### Добавляет комментарий к посту
> POST /posts/<<int:post_id>>/comments/
> ```json
> {
>    "author": "<author_name>",
>    "content": "<comment_content>"
> }
> ```