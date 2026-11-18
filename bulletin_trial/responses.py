def counts(rows, cells):
    totals = {key: {'returned':0, 'correct':0, 'missing':0} for key in cells}
    for row in rows:
        key = row['site'], row['round']
        value = row['correct']
        if value not in (True, False, None):
            raise ValueError('答题结果必须是对、错或未回应')
        target = totals[key]
        target['returned'] += value is not None
        target['correct'] += value is True
        target['missing'] += value is None
    return totals
