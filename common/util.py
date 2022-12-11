import logging
import os
import timeit

import mysql.connector
from dotenv import load_dotenv

logging.basicConfig(format='%(asctime)s [%(levelname)s]%(filename)s::%(funcName)s(%(lineno)s)'
                           '->%(message)s', level=logging.INFO)
log = logging.getLogger(__file__)

load_dotenv()

# Database connector
db_connection = mysql.connector.connect(
    host=os.getenv('HOST'),
    database=os.getenv('DATABASE'),
    user=os.getenv('ROOT'),
    passwd=os.getenv('PASS'),
)


def extract_data_from_cursor(cursor) -> dict[str, object]:
    log.info(f"got data{cursor}")
    result = None
    for data in cursor.fetchall():
        if result is None:
            result = {
                'headers': list(data.keys()),
                'data': [list(data.values())]
            }
        else:
            result['data'].append(list(data.values()))
    return result


def load_js():
    with open("VizzitProd/template/fetcher.js") as f:
        return timeit.timeit(f.read())
