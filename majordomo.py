import requests


def get_readings(sensor='TempSensor01.value', data='temperature', host='http://localhost/', type='7d'):
    readings = requests.get('%(host)s/pChart/?p=%(sensor)s&op=timed&type=%(type)s' % locals()).json()
    nice_readings = [{"dt": int(dt), data: float(value)} for dt, value in zip(readings['TIMES'], readings['VALUES'])]
    return nice_readings