# Бот-парсер Excel-файлов
Бот паспаршивает заполненные по шаблону Excel-файлы и сохраняет их в базу данных.

---
## Запуск приложения
В корневой папке скачанного репозитория выполните:
```
    python3 -m venv venv # use 'python' instead 'python3' for Win
    source venv/bin/activate # source venv/Scripts/activate for Win
    pip3 install -r requirements.txt
    python3 bot.py  # use 'python' instead 'python3' for Win
```

## Заполнение .env файла
Файл должен лежать в корневой директории
```
TELEGRAM_TOKEN=ur_telegram_token
```
 ---

## Технологии

- Python 3.9
- Aiogram
- SQlAlchemy
- Pandas