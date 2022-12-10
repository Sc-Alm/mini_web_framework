import json
import os
import jinja2
from dotenv import load_dotenv
from webob import Request, Response, static

from api.api import API
from common.util import log
from service import car, customer

load_dotenv()

app = API()
templateLoader = jinja2.FileSystemLoader(searchpath="templates/")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "index.html"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render()


@app.route("/")
def homepage(request:Request, response:Response):
    response.text = outputText
    response.content_type = "text/html"


@app.route("/api/task/2")
def get_rented_cars(request: Request, response: Response):
    response.json = json.dumps(car.get_cars_rented_between('2013-03-11', '2013-03-20'), default=str)
    response.content_type = "application/json"


@app.route("/api/task/1")
def get_phone_records(request: Request, response:Response):
    response.json = json.dumps(customer.get_customers_that_has_cellphones("CELL"))
    response.content_type = "application/json"


@app.route("/js/{name}")
def load_javascript(request: Request, response: Response, name: str):
    with open(f'templates/{name}') as f:
        response.text = f.read()
    response.content_type = 'application/javascript'


if __name__ == '__main__':
    log.info(car.get_cars_rented_between('2013-03-11', '2013-03-20'))
    log.info(customer.get_customers_that_has_cellphones('CELL'))
    print(os.getcwd())
