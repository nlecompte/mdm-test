FROM python:3.7

WORKDIR /app

COPY . .

ENV CORPUS=ab,ab,bc

RUN pip install -r requirements.txt


ENTRYPOINT ["python"]
CMD ["count/main.py"]