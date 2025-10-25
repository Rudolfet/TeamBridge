FROM python:3.11-slim

# Utente non-root
RUN useradd -m botuser
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV PYTHONUNBUFFERED=1
USER botuser
CMD ["python", "app.py"]
