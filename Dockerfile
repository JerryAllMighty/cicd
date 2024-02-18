FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV FLASK_APP "hello"
ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0", "-p 8080"]