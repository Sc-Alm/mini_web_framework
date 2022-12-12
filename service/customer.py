from common.util import db_connection, extract_data_from_cursor

SELECT_STATEMENT_PHONE_TEMPLATE = """
SELECT * FROM (
	SELECT CustomerId, COUNT(PhoneId) AS cnt FROM CustomerPhone GROUP BY CustomerId
) AS CT
INNER JOIN CustomerPhone C ON C.CustomerId = CT.CustomerId
INNER JOIN Phone P ON P.PhoneId = C.PhoneId
INNER JOIN Customer CU ON CU.CustomerId = C.CustomerId
WHERE CT.cnt > 1 AND PhoneType = '{phone_type}';
"""


def get_customers_that_has_cellphones(phone_type: str) -> dict[str, object]:
    with db_connection.cursor(dictionary=True) as cursor:
        cursor.execute(SELECT_STATEMENT_PHONE_TEMPLATE.format(phone_type=phone_type))
        return extract_data_from_cursor(cursor)
