''' Control of test cases, in this file we have the test cases that will be executed in endpoint tests.
'''
from datetime import datetime, timedelta
from decorators import ignore_warnings

CASES = {

    'CASE01': {
        'origin': 'CGH',
        'destination': 'SDU',
        'adults': 1,
        'promotion_code': 'ATH005'
    },
    'CASE02': {
        'origin': 'SDU',
        'destination': 'FLN',
        'going': datetime.now() + timedelta(30),
        'returning': datetime.now() + timedelta(34),
        'adults': 1,
        'promotion_code': 'ATH005'
    },
    'CASE03': {
        'origin': 'SDU',
        'destination': 'FLN',
        'adults': 2,
        'children': 1,
    },
    'CASE04': {
        'origin': 'SDU',
        'destination': 'FLN',
        'adults': 1,
        'infants': 1,
    },
    'CASE05': {
        'origin': 'CGH',
        'destination': 'GIG',
        'going': datetime.now() + timedelta(30),
        'adults': 1
    },
    'CASE06': {
        'origin': 'CGH',
        'destination': 'GIG',
        'going': datetime.now() + timedelta(30),
        'returning': datetime.now() + timedelta(32),
        'adults': 1
    },
    # NOTE: test sending cities in origin and destination international travel
    'CASE07': {
        'origin': 'SAO',
        'destination': 'MIA',
        'adults': 1,
    },
    'CASE08': {
        'origin': 'SAO',
        'destination': 'POA',
        'adults': 1,
    },
    # NOTE: est sending one of the most used itineraries
    'CASE11': {
        'origin': 'SDU',
        'destination': 'FLN',
        'adults': 1,
    },
    'CASE12': {
        'origin': 'GRU',
        'destination': 'GIG',
        'adults': 1,
        'children': 2,
    },
    'CASE09': {
        'origin': 'GRU',
        'destination': 'GIG',
        'adults': 1,
        'infants': 1,
    },
    'CASE10': {
        'origin': 'GRU',
        'destination': 'GIG',
        'adults': 1,
        'children': 2,
        'infants': 1,
    },

    'CASE11': {
        'origin': 'GRU',
        'destination': 'MAO',
        'adults': 1,
    },

    'CASE12': {
        'origin': 'GRU',
        'destination': 'JFK',
        'going': datetime.now() + timedelta(30),
        'adults': 1,
    },

    'CASE13': {
        'origin': 'JFK',
        'destination': 'GRU',
        'going': datetime.now() + timedelta(30),
        'adults': 1,
    },

    'CASE14': {
        'origin': 'JFK',
        'destination': 'SAO',
        'going': datetime(2020, 7, 18),
        'adults': 1,
    },
    
}


class TestingCases():
    
    def get_case(self, key_case):
        case = CASES[key_case]
        print("\n{}\n CASE: {}\n{}\n".format(
            "*" * 40, str(case), "*" * 40
        ))
        return case
    
    def _do_test(self, key_case):
        pass
    
    @ignore_warnings
    def test_CASE01(self):
        return self._do_test('CASE01')

    @ignore_warnings
    def test_CASE02(self):
        return self._do_test('CASE02')
'''
    @ignore_warnings
    def test_CASE03(self):
        return self._do_test('CASE03')

    @ignore_warnings
    def test_CASE04(self):
        return self._do_test('CASE04')

    @ignore_warnings
    def test_CASE05(self):
        return self._do_test('CASE05')

    @ignore_warnings
    def test_CASE06(self):
        return self._do_test('CASE06')

    @ignore_warnings
    def test_CASE07(self):
        return self._do_test('CASE07')

    @ignore_warnings
    def test_CASE08(self):
        return self._do_test('CASE08')

    @ignore_warnings
    def test_CASE09(self):
        return self._do_test('CASE09')

    @ignore_warnings
    def test_CASE11(self):
        return self._do_test('CASE11')
    
    @ignore_warnings
    def test_CASE12(self):
        return self._do_test('CASE12')

    @ignore_warnings
    def test_CASE13(self):
        return self._do_test('CASE13')

    @ignore_warnings
    def test_CASE14(self):
        return self._do_test('CASE14')
'''
