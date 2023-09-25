# Учебный проект: Foodgram - продуктовый помощник
### Описание:
Foodgram это веб сервис с помощью которого, пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список(в формате .txt) продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Как запустить проект:
#### API Foodgram локально:
1. Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:TheGreatestAriada/foodgram-project-react.git
```
```
cd foodgram-project-react
```
2. Cоздать и активировать виртуальное окружение:

* Если у вас Windows:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
* Если у вас Linux или macOS:
```
python3 -m venv venv
```
```
source venv/bib/activate
```
3. Установоить зависимости:
```
pip install -r requirements.txt
```
4. Перейти в дерикторию `foodgram/settings.py` заменить настройки базы данных на SQLite:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

5. Перейти в дерикторию `backend` выполнить миграции и создать супер пользователя:
```
cd backend
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
6. Наполнить базу данных ингредиентами:
```
python manage.py import_ingredients_from_csv
```
7. Запустить сервер разработки:
```
python manage.py runserver
```

**Проект будет досупен по адресу:**  
http://foodgramofariada.ddnsking.com

**Проект будет досупен по адресу:**  
Email адрес: admin@gmail.com  
Password: 325a325a325