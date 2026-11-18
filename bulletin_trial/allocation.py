def cells(rows, messages):
    topics = {row['message']: row['topic'] for row in messages}
    result = {}
    for row in rows:
        key = row['site'], row['round']
        mode = row['assigned'], row['actual']
        if key in result or not set(mode) <= {'paper', 'audio', None} or mode[0] is None:
            raise ValueError('轮次分派重复或形式无效')
        result[key] = {'assigned': mode[0], 'actual': mode[1], 'topic':topics[row['message']]}
    return result
