# Smart Traffic Management & Accident Response System

A portfolio-ready Python academic prototype combining:
- Adaptive traffic-signal timing from traffic density
- Emergency-vehicle priority
- Accident-event safety response
- Safe intersection state management
- Web dashboard/API
- Simulation mode for laptop demonstration

**Safety:** This is a software/academic simulation. It does not directly control public-road traffic signals.

## Priority hierarchy
1. Safety / accident response
2. Emergency vehicle priority
3. High-density traffic
4. Normal fair rotation

The controller conceptually passes through ALL-RED before changing the active direction.

## Run

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

Install:
```bash
pip install -r requirements.txt
```

Start:
```bash
python app.py
```

Open:
`http://127.0.0.1:5000`

Run tests:
```bash
python -m unittest discover -s tests -v
```

## Demo
The dashboard can simulate traffic density, an emergency vehicle, and an accident event.

API:
- GET `/api/state`
- POST `/api/simulate`
- POST `/api/next`
- POST `/api/reset`

## Future upgrades
- YOLO/OpenCV vehicle detection from CCTV/video
- Separately evaluated accident-detection model
- Multi-camera tracking
- SUMO traffic simulation
- Edge deployment
- Historical analytics

## Reference projects
High-level architecture ideas were reviewed from public repositories such as:
- MohamedRiyaz31/smart-traffic-management-ai-iot
- codewithtarun2005/traffic-management-system
- ARADHYA200/EMERGENCY_VEHICLE_DETECTION
- ShreyasLakshmikanth/Smart-Traffic-Simulation
- Dilkhush144/Smart-adaptive-traffic-light

This package is an original implementation. Do not copy code, datasets, model weights, screenshots, or documentation from other repositories unless their licenses allow it.
