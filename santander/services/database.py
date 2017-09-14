from pymongo import MongoClient
import time

connection = MongoClient('mongodb://heroku_wgqsrc8w:s98djebebkgm5m9iogan5kn1lr@ds045608.mlab.com:45608/heroku_wgqsrc8w')
db = connection['santander']


def get_all_funds():
    return db.funds.find({})


def insert(fund):
    if not exists(fund):
        db.funds.insert_one({"name": fund, "values": [], "profit": 1.0, "lastUpdate": "notToday"})


def get_fund(fund):
    return db.funds.find_one({"name": fund})


def exists(fund):
    print(fund)
    print(db.funds.find_one({"name": fund}))
    return db.funds.find_one({"name": fund}) is not None


def last_update_is(fund, date):
    return str(fund['lastUpdate']) == date


def insert_value(fund, value):
    date = time.strftime("%d/%m/%Y")
    fund = get_fund(fund)
    if not last_update_is(fund, date):
        profit = fund['profit'] * calculate_value(value)
        values = {"value": value, "date": date}
        db.funds.update({"name": fund['name']},
                        {"$push": {"values": values}, "$set": {"profit": profit, "lastUpdate": date}})


def insert_today_values(investments_founds_names, investments_founds_values):
    for i in range(len(investments_founds_names)):
        print(i)
        insert(investments_founds_names[i])
        print("fondo insertado")
        insert_value(investments_founds_names[i], investments_founds_values[i])
        print("valor insertado")


def calculate_value(value):
    if value < 0:
        res = 1 - abs(value) / 100
    else:
        res = 1 + (value / 100)
    return res
