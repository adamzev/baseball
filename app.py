from flask import Flask
from flask import render_template, request
from utils.utils import run_sim
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        print("post made")
        team1 = request.form.get('team1')
        team2 = request.form.get('team2')
        num_games = int(request.form.get('num_games'))
        data = run_sim(team1, team2, num_games)
        return render_template('index.html', **data)
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
