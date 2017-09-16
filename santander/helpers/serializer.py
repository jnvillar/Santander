def serialize_fund(fund):
    res = {
        'id': str(fund['_id']),
        'name': fund['name'],
        'profit': fund['profit'],
        'currency': fund['currency'],
        'link': fund['link'],
        'values': fund['values']
    }

    return res
