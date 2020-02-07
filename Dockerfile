FROM python:3.7

WORKDIR /app

COPY . .

ENV CORPUS=ab,ab,bc

RUN pip3 install .


ENTRYPOINT ["countcli"]