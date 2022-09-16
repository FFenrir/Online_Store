FROM python:3.8


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /OnlineStore


COPY Pipfile Pipfile.lock /OnlineStore/
RUN pip install pipenv && pipenv install --system
COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . /OnlineStore/