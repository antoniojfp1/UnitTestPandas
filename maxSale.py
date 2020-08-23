import pandas as pd

def readCsv(sales):
    cols = ["Manufacturer","Sales_in_thousands","Vehicle_type"]
    data = pd.read_csv(sales,usecols=cols)
    return data

def maxSale(data):
    totals = data.groupby("Manufacturer").sum("Sales_in_thousands")
    maximo = totals["Sales_in_thousands"].idxmax()
    print(maximo)
    return maximo

def mostSaleType(data):
    carType = data.groupby("Vehicle_type").count()
    maximo = carType["Manufacturer"].idxmax()
    print(maximo)
    return maximo

data = readCsv("Car_sales.csv")
maxSale(data)
mostSaleType(data)
