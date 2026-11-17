from controller import TrafficController
from detector import EventDetector

class SmartTrafficSystem:
    def __init__(self):
        self.controller = TrafficController()
        self.detector = EventDetector()

    def simulate(self, lane, vehicles, emergency=False, accident=False):
        event = self.detector.from_simulation(
            lane, emergency=emergency, accident=accident
        )
        self.controller.set_traffic(lane, vehicles)
        if event.accident:
            self.controller.report_accident(lane)
        elif event.emergency:
            self.controller.request_emergency(lane)
        return self.controller.snapshot()

    def reset(self):
        self.controller = TrafficController()
        return self.controller.snapshot()
