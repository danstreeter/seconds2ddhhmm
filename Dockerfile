FROM python:3.8-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP index.py

CMD [ "gunicorn", "-w 4", "-b 0.0.0.0:5000", "index:app" ]