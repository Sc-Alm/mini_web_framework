import os
import logging
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


def _convert_dict_to_parsable_dict(result_dict: dict) -> dict[str, object]:
    return {
        "headers": list(result_dict.keys()),
        "data": list(result_dict.values())
    }
