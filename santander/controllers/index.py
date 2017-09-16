from bson.json_util import dumps, loads
from flask import Blueprint, jsonify
import santander.services.database as db
from santander.helpers import scrapper

main = Blueprint('main', __name__)
scrapper_tool = scrapper.Scrapper()


@main.route('/ping')
def ping():
    return 'pong'


@main.route('/')
def investment_funds_all_values():
    funds = db.get_all_funds()
    funds = [
        {
            'id': str(fund['_id']),
            'name': fund['name'],
            'profit': fund['profit'],
            'currency': 'PESOS',
            'link': 'link',
            'value': fund['values'][-1]['value']
        }
        for fund in funds]

    funds = sorted(funds, key=lambda k: k['profit'], reverse=True)

    return jsonify(funds)


@main.route('/fund/<fund_id>')
def investment_fund_today_single_values(fund_id):
    fund = db.get_fund(fund_id)

    res = {
        'id': str(fund['_id']),
        'name': fund['name'],
        'profit': fund['profit'],
        'currency': 'PESOS',
        'link': 'link',
        'values': fund['values']
    }

    return jsonify(res)
