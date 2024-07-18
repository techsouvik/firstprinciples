FROM python:3.8-slim-buster
WORKDIR /app
COPY . .
RUN pip install pip==21.3.1
RUN pip3 install -r requirements.txt
CMD ["python", "app.py"]
