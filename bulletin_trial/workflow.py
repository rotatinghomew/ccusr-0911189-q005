from .allocation import cells
from .planning import gaps
from .responses import counts


def report(data):
    plan = cells(data['schedule'],data['messages'])
    responses = counts(data['returns'], plan)
    return {'cells':[{'site':site,'round':period,**plan[(site,period)],**responses[(site,period)]}
                     for site,period in sorted(plan)], 'unserved':gaps(data['schedule'])}
