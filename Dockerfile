FROM python:3.10.13-bullseye

ADD . .

RUN pip install -r requirements.txt

RUN python3 -m nltk.downloader stopwords

CMD python bot.py
