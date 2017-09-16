from flask import Blueprint, jsonify, request
import santander.services.database as db
from santander.helpers import scrapper, serializer

main = Blueprint('main', __name__)
scrapper_tool = scrapper.Scrapper()


@main.route('/ping')
def ping():
    return 'pong'


@main.route('/', methods=['GET'])
def index():
    order = request.args.get('order')

    if not order:
        order = "profit"

    funds = db.get_all_funds()
    funds = [
        {
            'id': str(fund['_id']),
            'name': fund['name'],
            'profit': fund['profit'],
            'currency': fund['currency'],
            'link': fund['link'],
            'value': fund['values'][-1]['value']
        }
        for fund in funds]

    funds = sorted(funds, key=lambda k: k[order], reverse=True)

    return jsonify(funds)


@main.route('/fund/<fund_id>')
def get_fund(fund_id):
    fund = serializer.serialize_fund(db.get_fund(fund_id))
    return jsonify(fund)


@main.route('/fund/edit/<fund_id>')
def edit_fund(fund_id):
    key = request.args.get('key')
    value = request.args.get('value')

    db.modify_value(fund_id, key, value)

    fund = serializer.serialize_fund(db.get_fund(fund_id))
    return jsonify(fund)
