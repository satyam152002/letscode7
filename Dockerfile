FROM python:slim
WORKDIR /app
COPY . .
EXPOSE 80
RUN pip install -r requirements.txt
CMD [ "python" ,"manage.py" ,"runserver","0.0.0.0:80"]