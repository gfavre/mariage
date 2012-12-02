from django.utils.datetime_safe import datetime, date


def mariage(request):
    value = date(2013, 8, 10)
    today = datetime.now()
    delta = value - today.date()
    
    return {'daysto': delta.days, 'over': delta.days < 0}
