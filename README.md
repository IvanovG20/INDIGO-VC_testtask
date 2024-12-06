## MINI-API ФИЛЬМОТЕКА

Сервис-фильмотека позволяющий зарегестрированым пользователям публиковать
фильмы и добавлять их в избранное. Незарегестрированым доступен только
просмотр и регистрация.

## Запуск проекта локально

Склонируйте репозиторий
```
git clone https://github.com/IvanovG20/indigo_testtask.git
```
Создайте и активируйте виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
После установки зависимостей перейдите в директорию indigo
```
cd indigo/
```
Создайте миграции
```
python manage.py makemigrations
```
Примените миграции
```
python manage.py migrate
```
В терминале пропишите команду запуска сервера
```
python manage.py runserver
```
Проект будет доступен по данному адресу
```
http://127.0.0.1:8000/
```

## Доступные эндпоинты
# Работа с пользователями
Создать пользователя
```
/api/users/
```
Аутентификация
```
/api/auth/token/login/
```
Профиль пользователя, изменить данные, удалить пользователя
```
/api/users/me/
```
# Работа с фильмами
Получить список фильмов, создать фильм
```
/api/films/
```
Получить, изменить, удалить фильм
```
/api/films/pk/
```
Добавить, удалить из избранного
```
/api/films/pk/favorite/
```
Список избранного для конкретного пользователи
```
/api/users/pk/favorites/
```
