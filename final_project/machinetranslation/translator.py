"""This is the python translation app

built with flask.
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

VERSION_LT = '2018-05-01'
authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(version=VERSION_LT, authenticator=authenticator)
language_translator.set_service_url(URL)


def english_to_french(english_text):
    """ translate english to france """
    translation_response = language_translator.translate(text=english_text, model_id='en-fr')
    translate = translation_response.get_result()
    # pylint: disable=unsubscriptable-object.
    french_text = translate['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """ translate french to english """
    translation_response = language_translator.translate(text=french_text, model_id='fr-en')
    translate = translation_response.get_result()
    # pylint: disable=unsubscriptable-object.
    english_text = translate['translations'][0]['translation']
    return english_text
