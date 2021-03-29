FROM python:3

RUN mkdir /app
RUN mkdir /app/static
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .

EXPOSE 8000



COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]
