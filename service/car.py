from typing import Dict

from common.util import db_connection, _convert_dict_to_parsable_dict

SELECT_STATEMENT_CAR_TEMPLATE = """
SELECT * FROM(
SELECT C.CarId FROM (
SELECT ColorId FROM booking.Color
WHERE ColorName LIKE 'Blue') AS CN
INNER JOIN booking.Car C ON C.ColorId = CN.ColorId) AS  CC
INNER JOIN booking.CustomerRental CR ON CR.CarId = CC.CarId
WHERE CR.RentFrom BETWEEN '{from_date}' AND '{to_date}'
OR CR.RentTo BETWEEN '{from_date}' AND '{to_date}'
"""


def _get_select_statement_for_rented_cars_between(from_date: str, to_date: str) -> str:
    return SELECT_STATEMENT_CAR_TEMPLATE.format(from_date=from_date, to_date=to_date)


def get_cars_rented_between(from_date: str, to_date: str) -> dict[str, object]:
    with db_connection.cursor(dictionary=True) as cursor:
        cursor.execute(SELECT_STATEMENT_CAR_TEMPLATE.format(from_date=from_date, to_date=to_date))
        for result in cursor.fetchall():
            return _convert_dict_to_parsable_dict(result)

