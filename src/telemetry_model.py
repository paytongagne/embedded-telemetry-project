from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Literal

DeviceStatus = Literal["nominal", "warning", "critical"]


@dataclass(frozen=True)
class TelemetryReading:
    device_id: str
    timestamp: str
    temperature_c: float
    voltage_v: float
    signal_dbm: int
    packet_loss_pct: float
    status: DeviceStatus

    def to_dict(self) -> dict:
        return asdict(self)


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def classify_status(
    temperature_c: float,
    voltage_v: float,
    signal_dbm: int,
    packet_loss_pct: float,
) -> DeviceStatus:
    if temperature_c >= 85 or voltage_v <= 3.1 or signal_dbm <= -90 or packet_loss_pct >= 12:
        return "critical"
    if temperature_c >= 75 or voltage_v <= 3.3 or signal_dbm <= -80 or packet_loss_pct >= 5:
        return "warning"
    return "nominal"


def validate_reading(reading: TelemetryReading) -> None:
    if not reading.device_id.strip():
        raise ValueError("device_id is required")
    if not -50 <= reading.temperature_c <= 150:
        raise ValueError("temperature_c outside expected range")
    if not 0 <= reading.voltage_v <= 24:
        raise ValueError("voltage_v outside expected range")
    if not -120 <= reading.signal_dbm <= 0:
        raise ValueError("signal_dbm outside expected range")
    if not 0 <= reading.packet_loss_pct <= 100:
        raise ValueError("packet_loss_pct outside expected range")
