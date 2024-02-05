import json
import random

# TODO: rename 'owner' to 'company'
OWNERS = ["EVgo", "ChargePoint", "ElectrifyAmerica", "Blink"]
SIZES = [50, 150, 350]  # TODO: Could write 50kw for string -> int munging
LAT_RANGE = [37.70,37.80]
LON_RANGE = [-122.50,-122.40]

# gen sites
NUM_SITES = 10
sites = []
site_baselines = {}
for i in range(1, NUM_SITES + 1):
    owner = random.choice(OWNERS)
    lat = random.uniform(LAT_RANGE[0], LAT_RANGE[1])
    lon = random.uniform(LON_RANGE[0], LON_RANGE[1])
    coords = [lat, lon]
    sites.append({"id": i, "owner": owner, "coords": coords})
    site_baselines[i] = random.choice(
        [10, 10, 10, 10, 20, 20, 30, 40, 50]
    )  # random.randint(10,50)

NUM_CHARGERS = 30
chargers = []
for i in range(1, NUM_CHARGERS + 1):
    size = random.choice(SIZES)
    site_id = (i % 10) + 1
    assert site_id >= 1 and site_id <= NUM_SITES
    usage = []
    baseline = site_baselines[site_id]
    for _ in range(24):
        minutes = baseline + random.randint(
            -10, 10
        )  # TODO: explore various distributions
        assert 0 <= minutes and minutes <= 60
        usage.append(minutes)
    chargers.append({"id": i, "site_id": site_id, "size": f"{size}kW", "usage": usage})

# tariffs = []
# * flat pricing: .3 per kWh
# * peak pricing:  .4 between 3pm and 9pm , otherwise .25
# * max use pricing: (per charger) .2 up to 1800 kWh usage, then .4 per kwh

with open("sites.json", "w") as f:
    json.dump(sites, f, indent = 1)
with open("chargers.json", "w") as f:
    json.dump(chargers, f, indent = 1)