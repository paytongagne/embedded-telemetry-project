from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Iterable

from telemetry_model import TelemetryReading

SCHEMA = """
CREATE TABLE IF NOT EXISTS telemetry_readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    temperature_c REAL NOT NULL,
    voltage_v REAL NOT NULL,
    signal_dbm INTEGER NOT NULL,
    packet_loss_pct REAL NOT NULL,
    status TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_telemetry_device_time
ON telemetry_readings(device_id, timestamp);
"""


def connect(database_path: str | Path = "telemetry.db") -> sqlite3.Connection:
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    connection.executescript(SCHEMA)
    return connection


def insert_reading(connection: sqlite3.Connection, reading: TelemetryReading) -> None:
    connection.execute(
        """
        INSERT INTO telemetry_readings (
            device_id, timestamp, temperature_c, voltage_v,
            signal_dbm, packet_loss_pct, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            reading.device_id,
            reading.timestamp,
            reading.temperature_c,
            reading.voltage_v,
            reading.signal_dbm,
            reading.packet_loss_pct,
            reading.status,
        ),
    )
    connection.commit()


def insert_batch(connection: sqlite3.Connection, readings: Iterable[TelemetryReading]) -> int:
    count = 0
    for reading in readings:
        insert_reading(connection, reading)
        count += 1
    return count


def latest_by_device(connection: sqlite3.Connection, device_id: str) -> dict | None:
    row = connection.execute(
        """
        SELECT * FROM telemetry_readings
        WHERE device_id = ?
        ORDER BY timestamp DESC, id DESC
        LIMIT 1
        """,
        (device_id,),
    ).fetchone()
    return dict(row) if row else None


def load_jsonl(path: str | Path) -> list[TelemetryReading]:
    readings: list[TelemetryReading] = []
    with Path(path).open("r", encoding="utf-8") as file:
        for line in file:
            item = json.loads(line)
            readings.append(TelemetryReading(**item))
    return readings
