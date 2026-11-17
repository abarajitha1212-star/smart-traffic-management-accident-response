from dataclasses import dataclass

@dataclass
class DetectionEvent:
    lane: str
    emergency: bool = False
    accident: bool = False
    confidence: float = 0.0
    source: str = "simulation"

class EventDetector:
    # Adapter layer for a future OpenCV/YOLO/model implementation.
    def from_simulation(self, lane, emergency=False, accident=False, confidence=0.99):
        return DetectionEvent(
            lane=lane,
            emergency=bool(emergency),
            accident=bool(accident),
            confidence=float(confidence),
            source="simulation",
        )
