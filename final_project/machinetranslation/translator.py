"""
    Translator functions
"""

# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICTOR = IAMAuthenticator(apikey=APIKEY)

LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2022-07-05',
    authenticator = AUTHENTICTOR
)

LANGUAGE_TRANSLATOR.set_service_url(service_url=URL)

def english_to_french(english_text):
    """
        Translate english to french
    """

    translation = LANGUAGE_TRANSLATOR.translate(
        text = english_text,
        model_id = "en-fr"
    ).get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
        Translate french to english
    """

    translation = LANGUAGE_TRANSLATOR.translate(
        text = french_text,
        model_id = 'fr-en'
    ).get_result()

    english_text = translation['translations'][0]['translation']
    return english_text
