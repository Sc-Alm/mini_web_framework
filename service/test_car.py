from unittest import TestCase
from datetime import datetime
from service.car import _get_select_statement_for_rented_cars_between, get_cars_rented_between

DESIERD_STATEMENT_TEMPLATE = """
select * from(
select C.CarId from(
select ColorId from booking.Color
where ColorName like 'Blue') as CN
inner join booking.Car C on C.ColorId = CN.ColorId) as  CC
inner join booking.CustomerRental CR on CR.CarId = CC.CarId
where CR.RentFrom between '2013-03-11' and '2013-03-20'
or CR.RentTo between '2013-03-11' and '2013-03-20'
"""



class Test(TestCase):
    def test__get_select_statment_for_rented_cars_between(self):
        self.assertEqual(_get_select_statement_for_rented_cars_between('2013-03-11', '2013-03-11'),
                         DESIERD_STATEMENT_TEMPLATE)

    def test_get_cars_rented_between(self):
        pass