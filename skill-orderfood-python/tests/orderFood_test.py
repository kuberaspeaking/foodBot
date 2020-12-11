import unittest
from impl.orderFood import skill


class MyTestCase(unittest.TestCase):
    def test_order_handler(self):
        '''
        to ensure that our implementation asks ' vegetarisch oder fliesch gerichte
        '''
        response = skill.test_intent('TEAM_29_ORDER_FOOD')
        self.assertEqual(response.text.key, 'ORDER_FOOD_MEAL_OPTIONS')


if __name__ == '__main__':
    unittest.main()
