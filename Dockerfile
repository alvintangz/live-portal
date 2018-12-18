FROM python:3.7

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN apt install unixodbc-dev
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "/code/manage.py", "runserver", "0.0.0.0:8000"]
# https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017