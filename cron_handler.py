import config
import majordomo
import sensehat
from feed_measurements import feed_measurement
from collections import defaultdict

readings = \
    sorted(
        majordomo.get_readings('TempSensor01.value', 'temperature', 'http://localhost/', '7d'),
        key=lambda x: x['dt']
    )[-1:]
readings += \
    sorted(
        majordomo.get_readings('HumSensor01.value', 'humidity', 'http://localhost/', '7d'),
        key=lambda x: x['dt']
    )[-1:]
readings += sensehat.pressure()


def compact_readings(r):
    dedup = defaultdict(dict)
    for reading in r:
        dedup[reading['dt']].update(reading)
    out = []
    for ts in sorted(dedup.keys()):
        out.append(dedup[ts])
    return out


readings = compact_readings(readings)

for r in readings:
    r['station_id'] = config.station_id

print(readings)
feed_measurement(readings)
