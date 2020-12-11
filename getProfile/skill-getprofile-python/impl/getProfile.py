import requests

from skill_sdk import skill, Response, tell, ask
from skill_sdk.l10n import _


@skill.intent_handler("ORDER_FOOD")
def handler() -> Response:
    """
    This handler is the first point of contact when your utterance is actually resolved!
    It will ask you what would you like to eat for lunch

    :return:        Response
    """
    msg = _('ORDER_FOOD_MEAL_OPTIONS')

    return tell(msg)

@skill.intent_handler("VEG")
def handler()-> Response:
    """
        This handler is the first point of contact when your utterance is actually resolved!
        it will list vegetarian options

        :return:        Response
        """
    try:
        # We request the vegetarian menu
        response = requests.get('https://kuberaspeaking.github.io/foodBot/assets/profile.json', timeout=10)
        # We parse the response json or raise exception if unsuccessful
        response.raise_for_status()
        data = response.json()
        # print(data)
        # We get the vegetarian menu from the response data
        menu = data['profile']['meal_choice']['vegetarisch']
        # We format our response to user or ask for an excuse
        veg = menu["keramikos"]+ menu["momos"]+ menu["Yarok"]+ menu["My Goodness"]
        if veg:
            msg = _("ORDER_FOOD_VEG", veg=veg)
        else:
            msg = _('ORDER_FOOD_RESPONSE_ERROR')
    except requests.exceptions.RequestException as err:
        msg = _('ORDER_FOOD_REQUEST_ERROR', err=err)

    return tell(msg)


@skill.intent_handler("HALLOUMI_SALAT")
def handler() -> Response:
    """
    Confirms your order
    :return:        Response
    """
    msg = _('ORDER_FOOD_HALLOUMI_SALAT')

    return tell(msg)

@skill.intent_handler("FRESH_DELIGHT")
def handler() -> Response:
    """
    Confirms your order
    :return:        Response
    """
    msg = _('ORDER_FOOD_FRESH_DELIGHT')

    return tell(msg)

@skill.intent_handler("MAKALI_SANDWICH")
def handler() -> Response:
    """
    Confirms your order
    :return:        Response
    """
    msg = _('ORDER_FOOD_MAKALI_SANDWICH')

    return tell(msg)

@skill.intent_handler("OVER_THE_RAINBOW")
def handler() -> Response:
    """
    Confirms your order
    :return:        Response
    """
    msg = _('ORDER_FOOD_OVER_THE_RAINBOW')

    return tell(msg)


@skill.intent_handler("FLEISCH")
def handler()-> Response:
    """
            This handler is the first point of contact when your utterance is actually resolved!
            it will list meat options

            :return:        Response
            """
    try:
        # We request the vegetarian menu
        response = requests.get('https://kuberaspeaking.github.io/foodBot/assets/profile.json', timeout=10)
        # We parse the response json or raise exception if unsuccessful
        response.raise_for_status()
        data = response.json()
        # print(data)
        # We get the meat menu from the response data
        menu = data['profile']['meal_choice']['Fleischgerichte']
        # We format our response to user or ask for an excuse
        fleisch = menu["keramikos"] + menu["Aiko Sushi"] + menu["Yarok"] + menu["Kuchi"]
        if fleisch:
            msg = _("ORDER_FOOD_VEG", fleisch=fleisch)
        else:
            msg = _('ORDER_FOOD_RESPONSE_ERROR')
    except requests.exceptions.RequestException as err:
        msg = _('ORDER_FOOD_REQUEST_ERROR', err=err)

    return tell(msg)



@skill.intent_handler("MOUSAKA")
def handler() -> Response:
    """
    Confirms your order
    :return:        Response
    """
    msg = _('ORDER_FOOD_MOUSAKA')

    return tell(msg)

@skill.intent_handler("KEBAB_SANDWICH")
def handler() -> Response:
    """
    Confirms your order
    :return:        Response
    """
    msg = _('ORDER_FOOD_KEBAB_SANDWICH')

    return tell(msg)

@skill.intent_handler("TORI_TERIYAKI")
def handler() -> Response:
    """
    Confirms your order
    :return:        Response
    """
    msg = _('ORDER_FOOD_TORI_TERIYAKI')

    return tell(msg)

@skill.intent_handler("MAKI_MIX_SPECIAL")
def handler() -> Response:
    """
    Confirms your order
    :return:        Response
    """
    msg = _('ORDER_FOOD_MAKI_MIX_SPECIAL')

    return tell(msg)
