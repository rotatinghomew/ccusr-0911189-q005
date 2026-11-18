def gaps(schedule):
    return sorted([row['site'], row['round']] for row in schedule if row['actual'] is None)
