from flask import Flask

#создаёт экземпляр класса Flask (переменную app)
app = Flask(__name__)
# Создаем секретный ключ для защиты данных:
app.config['SECRET_KEY'] = 'your_secret_key'
# Эта строка нужна, чтобы из пакета app импортировать все routs. Внутри rout мы будем прописывать пути.
from app import routes