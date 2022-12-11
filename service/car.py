from common.util import db_connection, extract_data_from_cursor

SELECT_STATEMENT_CAR_TEMPLATE = """
select * from(
select
    a.CarId,
    C.ColorId,
    a.RegistrationNumber,
    a.Milage
from Car a
inner join Color C on a.ColorId = C.ColorId
where C.ColorName like 'Blue') as BC
left join CustomerRental CR on BC.CarId = CR.CarId
WHERE RentFrom not BETWEEN '{from_date}' AND '{to_date}'
and RentTo not BETWEEN '{from_date}' AND '{to_date}'
or RentFrom is null;
"""


def _get_select_statement_for_rented_cars_between(from_date: str, to_date: str) -> str:
    return SELECT_STATEMENT_CAR_TEMPLATE.format(from_date=from_date, to_date=to_date)


def get_cars_rented_between(from_date: str, to_date: str) -> dict[str, object]:
    with db_connection.cursor(dictionary=True) as cursor:
        cursor.execute(SELECT_STATEMENT_CAR_TEMPLATE.format(from_date=from_date, to_date=to_date))
        return extract_data_from_cursor(cursor)
