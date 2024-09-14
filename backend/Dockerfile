FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install supabase

EXPOSE 8000

CMD ["python", "app.py"]
