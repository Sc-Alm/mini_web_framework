from unittest import TestCase
from datetime import datetime

from common.util import log
from service.car import _get_select_statement_for_rented_cars_between, get_cars_rented_between

DESIERD_STATEMENT_TEMPLATE = """
SELECT * FROM(
SELECT 
    A.CarId,
    C.ColorId,
    A.RegistrationNumber,
    A.Milage
FROM Car A
INNER JOIN Color C on A.ColorId = C.ColorId
WHERE C.ColorName LIKE 'Blue') AS BC
LEFT JOIN CustomerRental CR ON BC.CarId = CR.CarId
WHERE RentFrom NOT BETWEEN '{from_date}' AND '{to_date}'
AND RentTo NOT BETWEEN '{from_date}' AND '{to_date}'
OR RentFrom IS NULL;
"""
TEST_DATE_FROM = '2013-03-11'
TEST_DATE_TO = '2013-03-11'


class Test(TestCase):
    def test__get_select_statment_for_rented_cars_between(self):
        self.assertEqual(_get_select_statement_for_rented_cars_between('2013-03-11', '2013-03-11'),
                         DESIERD_STATEMENT_TEMPLATE)

    def test_get_cars_rented_between(self):
        result = get_cars_rented_between(TEST_DATE_FROM, TEST_DATE_TO)
        log.info(result)
        self.assertTrue(len(result['data']), 2)
