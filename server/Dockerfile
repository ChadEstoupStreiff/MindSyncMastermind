FROM python:3.11-slim-buster

# UPDATE
RUN pip install --upgrade pip
RUN apt-get update -y
RUN apt-get upgrade -y


# DEPENDENCIES
WORKDIR /

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt --default-timeout=100

# START
EXPOSE 8501
ENTRYPOINT ["python"]
CMD ["/app/main.py"]