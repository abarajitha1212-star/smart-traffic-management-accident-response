from flask import Flask, jsonify, request, render_template_string
from simulator import SmartTrafficSystem
from config import LANES

app = Flask(__name__)
system = SmartTrafficSystem()

HTML = '''
<!doctype html>
<html>
<head>
<title>Smart Traffic Management</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:Arial;margin:30px;background:#f4f6f8;color:#222}
.card{background:white;padding:20px;margin:12px 0;border-radius:12px}
button{padding:10px;margin:5px;border:0;border-radius:8px;cursor:pointer}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px}
</style>
</head>
<body>
<h1>Smart Traffic Management System</h1>
<div class="card">
<b>Active Lane:</b> <span id="active">-</span> |
<b>Phase:</b> <span id="phase">-</span> |
<b>Green Time:</b> <span id="green">-</span>s
<p id="message">-</p>
</div>
<div class="grid">
{% for lane in lanes %}
<div class="card">
<h3>{{lane}}</h3>
<label>Vehicles: <input id="v-{{lane}}" type="number" min="0" value="5"></label><br>
<button onclick="simulate('{{lane}}',false,false)">Traffic</button>
<button onclick="simulate('{{lane}}',true,false)">Emergency</button>
<button onclick="simulate('{{lane}}',false,true)">Accident</button>
</div>
{% endfor %}
</div>
<div class="card">
<button onclick="resetSystem()">Reset</button>
<button onclick="nextLane()">Next Lane</button>
</div>
<script>
async function refresh(){
 const r=await fetch('/api/state'); const s=await r.json();
 document.getElementById('active').textContent=s.active_lane;
 document.getElementById('phase').textContent=s.phase;
 document.getElementById('green').textContent=s.green_seconds;
 document.getElementById('message').textContent=s.message;
}
async function simulate(lane, emergency, accident){
 const vehicles=Number(document.getElementById('v-'+lane).value);
 await fetch('/api/simulate',{method:'POST',headers:{'Content-Type':'application/json'},
 body:JSON.stringify({lane,vehicles,emergency,accident})});
 refresh();
}
async function nextLane(){ await fetch('/api/next',{method:'POST'}); refresh(); }
async function resetSystem(){ await fetch('/api/reset',{method:'POST'}); refresh(); }
refresh();
</script>
</body>
</html>
'''

@app.get("/")
def home():
    return render_template_string(HTML, lanes=LANES)

@app.get("/api/state")
def state():
    return jsonify(system.controller.snapshot())

@app.post("/api/simulate")
def simulate():
    data = request.get_json(silent=True) or {}
    lane = data.get("lane")
    if lane not in LANES:
        return jsonify({"error": "Invalid lane"}), 400
    try:
        result = system.simulate(
            lane,
            int(data.get("vehicles", 0)),
            bool(data.get("emergency", False)),
            bool(data.get("accident", False)),
        )
        return jsonify(result)
    except (TypeError, ValueError) as exc:
        return jsonify({"error": str(exc)}), 400

@app.post("/api/next")
def next_lane():
    return jsonify({"active_lane": system.controller.next_lane(),
                    "state": system.controller.snapshot()})

@app.post("/api/reset")
def reset():
    return jsonify(system.reset())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
