FROM python:latest
MAINTAINER Devaki Kelkar "dakelkar@gmail.com"
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install  --index-url https://test.pypi.org/simple/ Flask-Bootstrap==4.0.0.0.dev2
RUN mkdir /app/logs
RUN touch /app/logs/service.log
COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]