from common.util import db_connection, extract_data_from_cursor

SELECT_STATEMENT_PHONE_TEMPLATE = """
select * from (
	select CustomerId, count(PhoneId) as cnt from CustomerPhone group by CustomerId
) as CT
INNER JOIN CustomerPhone C ON C.CustomerId = CT.CustomerId
INNER JOIN Phone P ON P.PhoneId = C.PhoneId
INNER JOIN Customer CU on CU.CustomerId = C.CustomerId
where CT.cnt > 1 and PhoneType = '{phone_type}';
"""


def get_customers_that_has_cellphones(phone_type: str) -> dict[str, object]:
    with db_connection.cursor(dictionary=True) as cursor:
        cursor.execute(SELECT_STATEMENT_PHONE_TEMPLATE.format(phone_type=phone_type))
        return extract_data_from_cursor(cursor)
