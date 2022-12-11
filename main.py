import json
import os
import timeit
import time
import jinja2
from dotenv import load_dotenv
from webob import Request, Response

from api.api import API
from common.util import log
from service import car, customer

load_dotenv()

app = API()
bcc = jinja2.FileSystemBytecodeCache('templates/jinja_cache_bucket')
templateLoader = jinja2.FileSystemLoader(searchpath="templates/")
templateEnv = jinja2.Environment(loader=templateLoader, bytecode_cache=bcc)
TEMPLATE_FILE = "index.html"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render()


@app.route("/")
def homepage(request: Request, response: Response):
    log.info("starter homepage")
    starttime = timeit.default_timer()
    response.text = outputText
    response.content_type = "text/html"
    print("The time difference is :", timeit.default_timer() - starttime)


@app.route("/api/task/2/{from_date}-{to_date}")
def get_rented_cars(request: Request, response: Response, from_date, to_date):
    starttime = timeit.default_timer()
    log.info(f"started transfer of data{from_date}-{to_date}")
    response.json = json.dumps(car.get_cars_rented_between(from_date, to_date), default=str)
    response.content_type = "application/json"

    print("the time difference is : ", timeit.default_timer() - starttime)


@app.route("/api/task/1")
def get_phone_records(request: Request, response: Response):
    response.json = json.dumps(customer.get_customers_that_has_cellphones("CELL"))
    response.content_type = "application/json"


@app.route("/js/{name}")
def load_javascript(request: Request, response: Response, name: str):
    log.info("starter loded js")
    starttime = timeit.default_timer()
    response.text = load_js(name)
    response.content_type = 'application/javascript'
    print("The time difference is :", timeit.default_timer() - starttime)


def load_js(name: str) -> str:
    with open(f'templates/{name}') as f:
        return f.read()


if __name__ == '__main__':
    log.info(car.get_cars_rented_between('2013-03-11', '2013-03-20'))
    log.info(customer.get_customers_that_has_cellphones('CELL'))
    print(os.getcwd())
