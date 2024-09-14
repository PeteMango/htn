FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py"]

# CMD ["sh", "-c", "pytest --maxfail=1 --disable-warnings -v && python manage.py"]
