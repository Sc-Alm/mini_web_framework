import os

from dotenv import load_dotenv

from api.api import API
from api.request_handler import RequestHandler
from api.respone_handler import ResponseHandler
from common.util import log
from service import car, customer
from service.page_loader import jinja_page_render

load_dotenv()

app = API()


@app.route("/")
def homepage(request: RequestHandler, response: ResponseHandler):
    log.info("starter homepage")
    response.set_body(body=jinja_page_render())
    response.set_header(header="Content-Type: text/html")


@app.route("/api/task/2/{from_date}@{to_date}")
def get_rented_cars(request: RequestHandler, response: ResponseHandler, from_date, to_date):
    log.info(f"started transfer of data{from_date}-{to_date}")
    response.set_json_body(json_body=car.get_cars_rented_between(from_date, to_date))
    response.set_header(header="Content-Type:application/json")


@app.route("/api/task/1")
def get_phone_records(request: RequestHandler, response: ResponseHandler):
    response.set_json_body(json_body=customer.get_customers_that_has_phone("CELL"))
    response.set_header(header="Content-Type:application/json")


if __name__ == '__main__':
    log.info(car.get_cars_rented_between('2013-03-11', '2013-03-20'))
    log.info(customer.get_customers_that_has_phone('CELL'))
    print(os.getcwd())
