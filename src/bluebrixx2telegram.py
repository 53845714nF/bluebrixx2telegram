#!/usr/bin/env python3
# coding=utf-8

'''
Telegram Bot send a Messege when BlueBrixx products are available.
'''


from os import getenv
from requests import post
from bluebrixx import product_available


print('Start Bluebrixx2telegram')

class UnconfiguredEnvironment(Exception):
    """base class for new exception"""
    pass

if not getenv('PRODUCT_URL', None):
    raise UnconfiguredEnvironment

if not getenv('TELEGRAM_TOKEN', None):
    raise UnconfiguredEnvironment

if not getenv('TELEGRAM_CHAT_ID', None):
    raise UnconfiguredEnvironment

URL = 'https://api.telegram.org/bot'
PRODUCT_URL = getenv('PRODUCT_URL')
TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = getenv('TELEGRAM_CHAT_ID')

def response():
    '''
    This function sends Messages by a response to keywords.
    '''
    post(URL + TELEGRAM_TOKEN + '/sendMessage', data={'chat_id': TELEGRAM_CHAT_ID,
                                                      'text': f'Your Bluebrixx product is available: { PRODUCT_URL }'
                                                     })

text, boolean = product_available(PRODUCT_URL)

if boolean:
    response()
    print('Send Message done')

print('Done')
