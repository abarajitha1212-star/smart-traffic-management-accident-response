import unittest
from controller import TrafficController

class TestTrafficController(unittest.TestCase):
    def test_high_density(self):
        c = TrafficController()
        c.set_traffic("North", 25)
        self.assertEqual(c.state.green_seconds, 40)

    def test_emergency_priority(self):
        c = TrafficController()
        c.request_emergency("West")
        self.assertEqual(c.state.active_lane, "West")

    def test_accident_safety_state(self):
        c = TrafficController()
        c.report_accident("East")
        self.assertEqual(c.state.phase, "ALL_RED")

if __name__ == "__main__":
    unittest.main()
