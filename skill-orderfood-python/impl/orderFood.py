import requests

from skill_sdk import skill, Response, tell, ask
from skill_sdk.l10n import _


HERE_APIKEY = "KUFJZlg1QpKnIqlMlodmDXeu7nNktr2-caRXFHpxgSI"


here_url = "https://browse.search.hereapi.com/v1/browse?apikey={}&in=circle:52.496345,13.355913;r=5000&categories=100-1000-0003&at=52.496345,13.355913&limit=3".format(HERE_APIKEY)



@skill.intent_handler("TEAM_29_ORDER_FOOD")
def handler() -> Response:
    """
    This handler is the first point of contact when your utterance is actually resolved!
    It will ask you what would you like to eat for lunch

    :return:        Response
    """
    try:
        response = requests.get(here_url)
        data = response.json()
        if(data["items"]):
            option1 = data["items"][0]["title"]
            option2 = data["items"][1]["title"]
            option3 = data["items"][2]["title"]
            msg = _('ORDER_FOOD_MEAL_OPTIONS', option1=option1, option2=option2, option3=option3)

    except requests.exceptions.RequestException as err:
        msg = _('ORDER_FOOD_REQUEST_ERROR', err=err)

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
    if (meal_type == "eins"):
        msg = _("ORDER_FOOD_OPTION1")

    if (meal_type == "zwei"):
        msg = _("ORDER_FOOD_OPTION2")

    if (meal_type == "drei"):
        msg = _("ORDER_FOOD_OPTION3")

    else:
        msg = _("ORDER_FOOD_RESPONSE_ERROR")

    return tell(msg)




