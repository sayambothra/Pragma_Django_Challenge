FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install django
RUN pip install djangorestframework
EXPOSE 8010
CMD ["python", "manage.py", "runserver", "0.0.0.0:8010"]
