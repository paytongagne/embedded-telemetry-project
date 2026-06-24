# Embedded Telemetry Project

Python-based telemetry simulation project for modeling connected-device health data, validation logic, status classification, and local database persistence.

This project is being built as a portfolio-ready systems project that connects embedded-style device data with backend processing and documentation.

## Overview

The project simulates telemetry readings from ESP32-style devices or lab sensors. Each reading includes device health metrics such as temperature, voltage, signal strength, packet loss, and a calculated status label.

The current version supports:

- Structured telemetry data models
- Synthetic telemetry generation
- Reading validation
- Device health classification
- JSONL sample output
- SQLite persistence
- Unit tests
- Architecture documentation

## Tech Stack

- Python
- SQLite
- JSON / JSONL
- pytest
- Backend data processing
- Embedded-style telemetry modeling

## Project Structure

```text
src/
  telemetry_model.py       Core data model, validation, and status logic
  telemetry_generator.py   Synthetic device telemetry generator
  telemetry_store.py       SQLite persistence layer

tests/
  test_sample_data.py      Starter test coverage
  test_telemetry_model.py  Telemetry validation and classification tests

docs/
  architecture.md          System design notes
  resume-bullets.md        Resume-safe project descriptions
```

## How to Run

Generate sample telemetry data:

```bash
python src/telemetry_generator.py
```

Run tests:

```bash
pytest
```

## Example Reading

```json
{
  "device_id": "esp32-lab-01",
  "timestamp": "2026-01-01T00:00:00+00:00",
  "temperature_c": 41.25,
  "voltage_v": 3.82,
  "signal_dbm": -62,
  "packet_loss_pct": 1.4,
  "status": "nominal"
}
```

## Roadmap

- Add REST API endpoints for device readings
- Add dashboard view for device health
- Add MQTT ingestion option
- Add Docker setup
- Add CSV export
- Add more tests around database queries

## Portfolio Purpose

This project demonstrates backend engineering fundamentals around simulated embedded telemetry, including clean data modeling, validation, persistence, testing, and architecture documentation.