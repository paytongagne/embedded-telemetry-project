# Embedded Telemetry Monitoring System Design

This document maps the next version of the telemetry monitoring project. The goal is to evolve the repository into a full backend monitoring system with simulated device data, validation, health classification, database persistence, API endpoints, tests, and dashboard documentation.

## System Layers

1. Device simulator
2. Telemetry validation
3. Health classification
4. Alert generation
5. SQLite storage
6. REST API
7. Dashboard view
8. Testing and CI

## Target Data Flow

```text
Device Simulator -> Telemetry Model -> Classifier -> Alert Engine -> Repository -> API -> Dashboard
```

## Core Metrics

- temperature_c
- voltage_v
- current_ma
- battery_percent
- signal_dbm
- memory_usage_percent
- uptime_seconds
- packet_sequence

## Health States

- NORMAL
- WARNING
- CRITICAL
- OFFLINE
- UNKNOWN

## Build Priorities

1. Create reusable models and thresholds.
2. Add database schema and repository methods.
3. Add FastAPI routes for devices, telemetry, alerts, and summaries.
4. Add dashboard files that consume the API.
5. Add tests for classifier, storage, simulator, and API behavior.
