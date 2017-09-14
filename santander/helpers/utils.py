from santander.services import database


def get_all_profit():
    funds = database.get_all_funds()
    res = {}
    for fund in funds:
        fund_name = fund['name']
        res[fund_name] = 0
        for value in fund['values']:
            print(type(value['value']))
            res[fund_name] += value['value']
    print(res)
