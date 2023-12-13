FROM ubuntu:latest
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN pip3 install django
RUN cd /app/expense_tracker_project
EXPOSE 8000
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
