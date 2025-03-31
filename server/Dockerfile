# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы с кодом сервера
COPY server.py player.py requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для подключения клиентов
EXPOSE 5555

# Запускаем сервер при старте контейнера
CMD ["python", "server.py"]