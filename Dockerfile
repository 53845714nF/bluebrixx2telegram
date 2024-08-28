FROM python:3.11-alpine

WORKDIR /app

RUN apk add --no-cache tzdata
ENV TZ=Europe/Berlin

COPY pyproject.toml ./
RUN pip install -e .

COPY /src /app

RUN echo "0 9 * * * python -m telegram.telegram" >> /var/spool/cron/crontabs/root
RUN echo "0 12 * * * python -m telegram.telegram" >> /var/spool/cron/crontabs/root
RUN echo "0 18 * * * python -m telegram.telegram" >> /var/spool/cron/crontabs/root

CMD ["crond", "-f"]
