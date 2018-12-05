FROM python:3.7

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN apt install unixodbc-dev
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "/code/manage.py", "runserver", "0.0.0.0:8000"]