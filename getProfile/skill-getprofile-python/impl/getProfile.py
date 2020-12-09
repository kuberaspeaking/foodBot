import random
import json

from skill_sdk import skill, Response, tell, Card
from skill_sdk.l10n import _

INTENT_NAME = 'GET_MENU'
#
# PROFILE_BASE_URL = "https://kuberaspeaking.github.io/foodBot/assets/profile.json"



def get_profile_url() -> str:
    """
    reads the menu options for the user

    :return:
    """
    with open('static/profile.json') as f:
        data = json.load(f)

    menu = data["profile"]

    print(menu["meal_choice"])

    return menu


@skill.intent_handler(INTENT_NAME)
def handler() -> Response:
    """
    This handler is the first point of contact when your utterance is actually resolved!
    It will make sure to send you funny memes to your phone.

    :return:        Response
    """
    # We get a translated message
    msg = _('What would you like to eat today?')
    # We create a simple response
    response = tell(msg)
    response.card = Card(
        title=_("options"),
        action=get_profile_url(),
        action_text=_("options->menu")
    )

    return response

