from flask import Flask, request, jsonify

app = Flask(__name__)

players = []
matches = []

@app.route('/players', methods=['GET'])
def get_players():
    return jsonify(players)

@app.route('/players', methods=['POST'])
def add_player():
    player = request.json
    players.append(player)
    return jsonify(player), 201

@app.route('/matches', methods=['GET'])
def get_matches():
    return jsonify(matches)

@app.route('/matches', methods=['POST'])
def schedule_match():
    match = request.json
    matches.append(match)
    return jsonify(match), 201

if __name__ == '__main__':
    app.run(debug=True)






