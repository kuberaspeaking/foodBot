import random
import json
import requests

from skill_sdk import skill, Response, tell, Card
from skill_sdk.l10n import _


@skill.intent_handler("ORDER_FOOD")
def handler() -> Response:
    """
    This handler is the first point of contact when your utterance is actually resolved!
    It will make sure to send you funny memes to your phone.

    :return:        Response
    """
    try:
        # We request a random joke from icndb with time-out set to 10 seconds
        response = requests.get('https://kuberaspeaking.github.io/foodBot/assets/profile.json', timeout=10)
        # We parse the response json or raise exception if unsuccessful
        response.raise_for_status()
        data = response.json()
        print(data)
        # We get the menu from the response data
        menu = data['profile']['meal_choice']
        # We format our response to user or ask for an excuse
        if menu:
            msg = _('Was möchtest du essen? Vegetarisch oder Fleischgerichte?', menu=menu)
        else:
            msg = _('Ich verstehe nicht')
    except requests.exceptions.RequestException as err:
        msg = _('ERROR', err=err)

        # We create a response with either menu or error message
    return tell(msg)



