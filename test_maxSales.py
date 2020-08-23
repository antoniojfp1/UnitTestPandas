import maxSale
import pytest

data = maxSale.readCsv("Car_sales.csv")

def test_for_ok_maxSales():
    assert maxSale.maxSale(data) == "Ford"

def test_for_missing_maxSales():
    assert maxSale.maxSale(data) != "Mazda"

def test_for_ok_mostSaleType():
    assert maxSale.mostSaleType(data) == "Passenger"

def test_for_missing_mostSaleType():
    assert maxSale.mostSaleType(data) == "Car"