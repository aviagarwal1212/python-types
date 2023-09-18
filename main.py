from typing import TypedDict, Required, NotRequired


class Coordinate(TypedDict):
    x: float
    y: float
    label: str
    category: NotRequired[str]


coordinate: Coordinate = {"x": 10, "y": 20, "label": "Profit"}


Vote = TypedDict("Vote", {"for": int, "against": int})
vote: Vote = {"for": 100, "against": 200}
