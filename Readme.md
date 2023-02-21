# Bluebrixx2telegram

## Description
A scraper for the website `https://www.bluebrixx.com/de/` which checks if a certain product is available.
If this product is available, a Telegram message will be sent.

## Usage

To start the project, docker and are required. The installation instructions can be found here.

Pull the docker Image: `docker pull ghcr.io/53845714nf/bluebrixx2telegram/bluebrixx2telegram:latest`


Example to start (Change the env values to yours.) :

```bash
sudo docker run -d \
-e "PRODUCT_URL=https://www.bluebrixx.com/de/pirates/105326/Gouverneursinsel-Wachturm-Erweiterung-BlueBrixx-Special" \
-e "TELEGRAM_TOKEN=678901234:bkhuifewhfhewrheulqrkjreqhtiuqweh" \
-e "TELEGRAM_CHAT_ID=545678900" \
bluebrixx2telegram
```

## Building your own Image

```
sudo docker build . -t bluebrixx2telegram
```
