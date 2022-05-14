import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    """
    Main page: help and list of available endpoints
    """
    return jsonify({
        'endpoints': {
            'POST': {
                '/solve': 'Solve a game : send a game with JSON format in body',
            },
            'GET': {
                '/new': 'Return a new random game',
                '/complete': 'Send a new random game and the solution'
            }
        },
        'creator': 'Corentin Le Guen',
        'contact': 'leguen.corentin@protonmail.com'
    })


@app.route("/solve", methods=['POST'])
def solve():
    """
    Solve a game: receive game by json body
    """
    from flask import request
    msg = request.get_json()

    bad_message_format = 'bad message, try the /new endpoint to an example message'

    if msg.get('numbers') is None or msg.get('target') is None:
        return jsonify({
            'error': bad_message_format
        }), 400

    from lceb import runit
    try:
        solution = runit(msg)
        return jsonify({
            'game': msg,
            'solution': solution
        })
    except TypeError or KeyError:
        return jsonify({
            'error': bad_message_format
        }), 400


@app.route("/new")
def new():
    """
    Send a random game: json body
    """
    from lceb import new_game
    return jsonify(new_game())


@app.route("/complete")
def complete():
    """
    Send both new game and solution with json format
    """
    from lceb import new_game
    game = new_game()
    from lceb import runit
    solution = runit(game)
    return jsonify({
        'game': game,
        'solution': solution
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
