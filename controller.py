from dataclasses import dataclass, field
from typing import Dict, Optional
from config import LANES, MIN_GREEN, MAX_GREEN, DENSITY_HIGH, DENSITY_MEDIUM

@dataclass
class TrafficState:
    active_lane: str = "North"
    phase: str = "GREEN"
    green_seconds: int = MIN_GREEN
    vehicles: Dict[str, int] = field(default_factory=lambda: {lane: 0 for lane in LANES})
    emergency_lane: Optional[str] = None
    accident_lane: Optional[str] = None
    message: str = "Normal adaptive control"

class TrafficController:
    def __init__(self):
        self.state = TrafficState()

    def set_traffic(self, lane, vehicles):
        if lane not in LANES:
            raise ValueError("Invalid lane")
        self.state.vehicles[lane] = max(0, int(vehicles))
        self._update_green_time()

    def _update_green_time(self):
        count = self.state.vehicles[self.state.active_lane]
        if count >= DENSITY_HIGH:
            self.state.green_seconds = MAX_GREEN
        elif count >= DENSITY_MEDIUM:
            self.state.green_seconds = 25
        else:
            self.state.green_seconds = MIN_GREEN

    def request_emergency(self, lane):
        if lane not in LANES:
            raise ValueError("Invalid lane")
        self.state.emergency_lane = lane
        self._safe_switch(lane)
        self.state.message = f"Emergency priority granted to {lane}"

    def report_accident(self, lane):
        if lane not in LANES:
            raise ValueError("Invalid lane")
        self.state.accident_lane = lane
        self.state.phase = "ALL_RED"
        self.state.message = f"Accident reported on {lane}; safety response active"

    def clear_accident(self):
        self.state.accident_lane = None
        self.state.phase = "GREEN"
        self.state.message = "Accident cleared; adaptive control resumed"
        self._update_green_time()

    def _safe_switch(self, lane):
        self.state.phase = "ALL_RED"
        self.state.active_lane = lane
        self.state.phase = "GREEN"
        self._update_green_time()

    def next_lane(self):
        if self.state.accident_lane:
            return self.state.active_lane
        if self.state.emergency_lane:
            lane = self.state.emergency_lane
            self.state.emergency_lane = None
            self._safe_switch(lane)
            return lane
        idx = LANES.index(self.state.active_lane)
        lane = LANES[(idx + 1) % len(LANES)]
        self._safe_switch(lane)
        self.state.message = f"Normal adaptive rotation: {lane}"
        return lane

    def snapshot(self):
        return {
            "active_lane": self.state.active_lane,
            "phase": self.state.phase,
            "green_seconds": self.state.green_seconds,
            "vehicles": self.state.vehicles,
            "emergency_lane": self.state.emergency_lane,
            "accident_lane": self.state.accident_lane,
            "message": self.state.message,
        }
