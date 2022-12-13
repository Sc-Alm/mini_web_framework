import json
import os
import uwsgidecorators
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
    response.text = outputText
    response.content_type = "text/html"


@app.route("/api/task/2/{from_date}@{to_date}")
def get_rented_cars(request: Request, response: Response, from_date, to_date):
    log.info(f"started transfer of data{from_date}-{to_date}")
    response.json = json.dumps(car.get_cars_rented_between(from_date, to_date), default=str)
    response.content_type = "application/json"


@app.route("/api/task/1")
def get_phone_records(request: Request, response: Response):
    response.json = json.dumps(customer.get_customers_that_has_phone("CELL"))
    response.content_type = "application/json"


if __name__ == '__main__':
    log.info(car.get_cars_rented_between('2013-03-11', '2013-03-20'))
    log.info(customer.get_customers_that_has_phone('CELL'))
    print(os.getcwd())
