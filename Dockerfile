FROM python:3.5
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
WORKDIR /app/react_blog/
EXPOSE 8000
