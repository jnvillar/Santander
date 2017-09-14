from flask import Blueprint
from flask import jsonify

import santander.services.database as database
from santander.helpers import scrapper
from bson.json_util import dumps

main = Blueprint('main', __name__)
scrapper_tool = scrapper.Scrapper()


@main.route('/a')
def ping():
    return 'pong'


@main.route('/fondos')
def investment_funds_today_value():
    funds = database.get_all_funds()
    funds = [doc for doc in funds]
    return dumps(funds)


@main.route('/')
def investment_funds_all_values():
    investments_founds_names = scrapper_tool.get_investment_founds()
    investments_founds_values = scrapper_tool.get_investment_founds_today_values()
    sub_list = [investments_founds_values[n:n + 5] for n in range(0, len(investments_founds_values), 5)]

    res = []
    for investments_found, values in zip(investments_founds_names, sub_list):
        obj = dict()
        obj['name'] = investments_found
        obj['values'] = values
        res.append(obj)

    return jsonify(res)
