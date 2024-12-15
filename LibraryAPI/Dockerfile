FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .
COPY src/models/ src/models/
COPY static/ static/

CMD ["python", "app.py"]