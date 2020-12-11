import requests

from skill_sdk import skill, Response, tell, ask
from skill_sdk.l10n import _


@skill.intent_handler("TEAM_29_ORDER_FOOD")
def handler() -> Response:
    """
    This handler is the first point of contact when your utterance is actually resolved!
    It will ask you what would you like to eat for lunch

    :return:        Response
    """
    msg = _('ORDER_FOOD_MEAL_OPTIONS')

    return ask(msg)

@skill.intent_handler("TEAM_29_FOODBOT")
def handler() -> Response:
    """
    This handler is the first point of contact when your utterance is actually resolved!
    It will ask you what would you like to eat for lunch

    :return:        Response
    """
    msg = _('ORDER_FOOD_OVERVIEW')

    return tell(msg)


@skill.intent_handler("TEAM_29_MEAL_TYPE")
def handler(meal_type: str)-> Response:
    """
        This handler is the first point of contact when your utterance is actually resolved!
        it will list vegetarian options

        :return:        Response
    """
    if (meal_type.lower() == "vegetarian"):
        msg = _("ORDER_FOOD_VEG")

    if (meal_type.lower() == "fleischgerichte"):
        msg = _("ORDER_FOOD_FLIESCH")

    else:
        msg = _("ORDER_FOOD_RESPONSE_ERROR")

    return tell(msg)




