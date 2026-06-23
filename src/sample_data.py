import json
import random
from datetime import datetime


def make_sample_reading(name):
    temp = round(random.uniform(20.0, 75.0), 2)
    battery = round(random.uniform(3.2, 4.2), 2)
    state = "review" if temp > 60 or battery < 3.4 else "normal"

    return {
        "name": name,
        "time": datetime.utcnow().isoformat(),
        "temperature": temp,
        "battery": battery,
        "state": state,
    }


def main():
    records = [make_sample_reading(f"unit-{i}") for i in range(1, 6)]
    print(json.dumps(records, indent=2))


if __name__ == "__main__":
    main()
