from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Iterable

from telemetry_model import TelemetryReading, classify_status, utc_timestamp, validate_reading


def generate_reading(device_id: str, rng: random.Random | None = None) -> TelemetryReading:
    rng = rng or random.Random()
    temperature_c = round(rng.uniform(28.0, 92.0), 2)
    voltage_v = round(rng.uniform(3.0, 4.2), 2)
    signal_dbm = rng.randint(-96, -45)
    packet_loss_pct = round(rng.uniform(0.0, 15.0), 2)
    status = classify_status(temperature_c, voltage_v, signal_dbm, packet_loss_pct)

    reading = TelemetryReading(
        device_id=device_id,
        timestamp=utc_timestamp(),
        temperature_c=temperature_c,
        voltage_v=voltage_v,
        signal_dbm=signal_dbm,
        packet_loss_pct=packet_loss_pct,
        status=status,
    )
    validate_reading(reading)
    return reading


def generate_batch(device_ids: Iterable[str], samples_per_device: int = 5, seed: int = 42) -> list[TelemetryReading]:
    rng = random.Random(seed)
    readings: list[TelemetryReading] = []
    for device_id in device_ids:
        for _ in range(samples_per_device):
            readings.append(generate_reading(device_id, rng))
    return readings


def write_jsonl(readings: Iterable[TelemetryReading], output_path: str | Path) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        for reading in readings:
            file.write(json.dumps(reading.to_dict()) + "\n")


if __name__ == "__main__":
    batch = generate_batch(["esp32-lab-01", "esp32-lab-02", "sim-node-01"], samples_per_device=10)
    write_jsonl(batch, "data/sample_telemetry.jsonl")
    print(f"Generated {len(batch)} telemetry readings in data/sample_telemetry.jsonl")
