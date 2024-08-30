#!/usr/bin/env python3
# coding=utf-8

"""
Telegram Bot send a Messege when BlueBrixx products are available.
"""

from os import getenv

from requests import post

from bluebrixx import product_available


class UnconfiguredEnvironment(Exception):
    """
    base class for new exception
    """

    pass


def send_message_to_telegram(token: str, chat_id: str, product_url: str):
    """
    This function sends Messages
    by a response to keywords.
    """
    post(
        "https://api.telegram.org/bot" + token + "/sendMessage",
        data={
            "chat_id": chat_id,
            "text": f"Your Bluebrixx product is available: {product_url}",
        },
    )


def telegram_bot():
    print("Start Bluebrixx2telegram")

    if not getenv("PRODUCT_URL", None):
        print("PRODUCT_URL not found")
        raise UnconfiguredEnvironment

    if not getenv("TELEGRAM_TOKEN", None):
        print("TELEGRAM_TOKEN not found")
        raise UnconfiguredEnvironment

    if not getenv("TELEGRAM_CHAT_ID", None):
        print("TELEGRAM_CHAT_ID not found")
        raise UnconfiguredEnvironment

    PRODUCT_URL = getenv("PRODUCT_URL")
    TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN")
    TELEGRAM_CHAT_ID = getenv("TELEGRAM_CHAT_ID")

    text, available = product_available(PRODUCT_URL)
    print(f"Current status: {text}")

    if available:
        send_message_to_telegram(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, PRODUCT_URL)
        print("Send Telegram Message done")

    print("Done with fetch")


if __name__ == "__main__":
    telegram_bot()
