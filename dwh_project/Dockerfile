# Используем базовый образ Python 3.10.9
FROM python:3.10.9

## Устанавливаем переменную окружения для Django
ENV PYTHONUNBUFFERED 1

# Создаем директорию /app внутри контейнера
RUN mkdir /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект Django в контейнер
COPY . /app/

# Открываем порт, на котором будет работать приложение
EXPOSE 8000

# Запускаем сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]