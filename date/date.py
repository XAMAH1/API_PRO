def date(curentdate):
    date = curentdate.split('.')
    newdate = f'{date[2]}-{date[1]}-{date[0]}'
    return newdate