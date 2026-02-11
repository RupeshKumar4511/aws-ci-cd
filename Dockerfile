FROM python:3.11

WORKDIR /app

COPY requiremets.txt .

RUN pip install -r requiremets.txt

COPY . .

EXPOSE 5000

CMD ["python","app.py"]