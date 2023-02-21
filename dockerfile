FROM python:3.9-alpine

RUN apk add --no-cache tzdata
ENV TZ=Europe/Berlin

WORKDIR /app

COPY /src /app
RUN pip install -r requirements.txt

RUN echo "0 9 * * * /app/bluebrixx2telegram.py" >> /var/spool/cron/crontabs/root
RUN echo "0 12 * * * /app/bluebrixx2telegram.py" >> /var/spool/cron/crontabs/root
RUN echo "0 18 * * * /app/bluebrixx2telegram.py" >> /var/spool/cron/crontabs/root

CMD crond -f
