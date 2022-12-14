from common.util import extract_data_from_cursor, get_db_connection

SELECT_STATEMENT_CAR_TEMPLATE = """
SELECT * FROM(
SELECT 
    A.CarId,
    C.ColorId,
    A.RegistrationNumber,
    A.Milage
FROM Car A
INNER JOIN Color C on A.ColorId = C.ColorId
WHERE C.ColorName LIKE '{car_colour}') AS BC
LEFT JOIN CustomerRental CR ON BC.CarId = CR.CarId
WHERE RentFrom NOT BETWEEN '{from_date}' AND '{to_date}'
AND RentTo NOT BETWEEN '{from_date}' AND '{to_date}'
OR RentFrom IS NULL;
"""


def _get_select_statement_for_rented_cars_between(from_date: str, to_date: str) -> str:
    return SELECT_STATEMENT_CAR_TEMPLATE.format(from_date=from_date, to_date=to_date)


def get_cars_rented_between(from_date: str, to_date: str, car_colour: str) -> dict[str, object]:
    with get_db_connection().cursor(dictionary=True) as cursor:
        print(SELECT_STATEMENT_CAR_TEMPLATE.format(from_date=from_date,
                                                   to_date=to_date,
                                                   car_colour=car_colour))
        cursor.execute(SELECT_STATEMENT_CAR_TEMPLATE.format(from_date=from_date,
                                                            to_date=to_date,
                                                            car_colour=car_colour))
        return extract_data_from_cursor(cursor)
