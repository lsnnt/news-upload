FROM python:3

LABEL org.opencontainers.image.source=https://github.com/lsnnt/news-upload
LABEL org.opencontainers.image.description="news-uploading to scribd via program"
LABEL org.opencontainers.image.licenses="GPL-3.0-or-later"


WORKDIR /app
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


CMD [ "python", "./main.py" ]
