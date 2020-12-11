#
# voice-skill-sdk
#
# (C) 2020, YOUR_NAME (YOUR COMPANY), Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
import unittest
from impl.getProfile import skill


class TestMain(unittest.TestCase):

    def test_order_handler(self):
        """ A simple test case to ensure that our implementation asks 'vegetarisch oder Fleishgerichte'
        """
        response = skill.test_intent('ORDER_FOOD')
        self.assertEqual(response.text.key, 'ORDER_FOOD_MEAL_OPTIONS')

