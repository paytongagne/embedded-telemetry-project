import pytest

from src.telemetry_model import TelemetryReading, classify_status, validate_reading


def test_status_nominal_when_values_are_healthy():
    assert classify_status(40.0, 3.8, -55, 1.0) == "nominal"


def test_status_warning_when_temperature_is_elevated():
    assert classify_status(76.0, 3.8, -55, 1.0) == "warning"


def test_status_critical_when_voltage_is_low():
    assert classify_status(40.0, 3.0, -55, 1.0) == "critical"


def test_validation_rejects_missing_device_id():
    reading = TelemetryReading(
        device_id="",
        timestamp="2026-01-01T00:00:00+00:00",
        temperature_c=40.0,
        voltage_v=3.8,
        signal_dbm=-55,
        packet_loss_pct=1.0,
        status="nominal",
    )

    with pytest.raises(ValueError):
        validate_reading(reading)
