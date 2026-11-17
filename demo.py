from simulator import SmartTrafficSystem

system = SmartTrafficSystem()
print("Normal:", system.simulate("North", 8))
print("High density:", system.simulate("East", 25))
print("Emergency:", system.simulate("South", 12, emergency=True))
print("Accident:", system.simulate("West", 6, accident=True))
