# Architecture

This project models a small telemetry pipeline similar to what might be used for connected hardware, lab devices, or embedded sensor systems.

## Current Workflow

```text
Simulated Device IDs
        |
        v
Telemetry Generator
        |
        v
Validated Reading Model
        |
        v
JSONL sample data or SQLite storage
        |
        v
Future dashboard/API layer
```

## Components

### Telemetry model

`src/telemetry_model.py` defines the core reading structure and the status classification logic.

Each reading includes:

- Device ID
- UTC timestamp
- Temperature
- Voltage
- Signal strength
- Packet loss
- Status

### Telemetry generator

`src/telemetry_generator.py` creates repeatable sample readings for simulated devices. This makes the project easy to test without physical hardware.

### Storage layer

`src/telemetry_store.py` persists readings to SQLite and provides a lookup for the latest reading by device.

## Design Goals

- Keep the first version lightweight and easy to run locally
- Separate data generation, validation, and persistence logic
- Make the code testable before adding dashboards or external services
- Leave a clear path toward MQTT, REST APIs, and embedded hardware input

## Planned Additions

- REST API for latest telemetry readings
- Dashboard view for device health
- MQTT ingestion option
- Docker setup for local development
- CSV/JSON export options
