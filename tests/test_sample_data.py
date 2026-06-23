from src.sample_data import make_sample_reading


def test_sample_reading_has_expected_fields():
    record = make_sample_reading("unit-test")

    assert record["name"] == "unit-test"
    assert "time" in record
    assert "temperature" in record
    assert "battery" in record
    assert "state" in record


def test_state_is_valid():
    record = make_sample_reading("unit-test")
    assert record["state"] in {"normal", "review"}
