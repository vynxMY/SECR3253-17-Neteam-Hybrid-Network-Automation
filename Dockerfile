FROM python:3.11

WORKDIR /app

COPY . .

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

CMD ["python3", "main.py"]
