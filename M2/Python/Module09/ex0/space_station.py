from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    print("=== VALID SPACE STATION ===")

    try:
        station = SpaceStation(
            station_id="SS001",
            name="Alpha Station",
            crew_size=10,
            power_level=85.5,
            oxygen_level=92.0,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="Main research station"
        )

        print(f"Station ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew Size: {station.crew_size}")
        print(f"Power Level: {station.power_level}%")
        print(f"Oxygen Level: {station.oxygen_level}%")
        print(f"Last Maintenance: {station.last_maintenance}")
        print(f"Operational: {station.is_operational}")
        print(f"Notes: {station.notes}")

    except ValidationError as e:
        print("Validation Error:")
        print(e)

    print("\n=== INVALID SPACE STATION ===")

    try:
        bad_station = SpaceStation(
            station_id="SS002",
            name="Broken Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=60.0,
            last_maintenance=datetime.now(),
            is_operational=False,
            notes="Testing validation errors"
        )

        print(bad_station)

    except ValidationError as e:
        print("Validation Error:")
        print(e)


if __name__ == "__main__":
    main()
