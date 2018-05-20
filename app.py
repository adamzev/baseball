import os

from flask import (
    Flask, 
    send_from_directory,
    render_template,
    request
)
from utils.utils import run_sim
import json

app = Flask(__name__, static_folder='frontend/build')

@app.route('/api/simulation', methods=["POST"])
def simulation():
    data = request.get_json()
    team1, team2, num_games = data['team1'], data['team2'], data['num_games']
    print(team1, team2, num_games)
    results = run_sim(team1, team2, num_games)
    print(results)
    return json.dumps(results)

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("frontend/build/" + path):
        return send_from_directory('frontend/build', path)
    else:
        return send_from_directory('frontend/build', 'index.html')
