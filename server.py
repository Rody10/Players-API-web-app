from flask import Flask, render_template, request
from flask_restful import Api, Resource, abort


app = Flask(__name__)
app.config['SECRET_KEY'] = 'lcv3sb[M/^|QT.]@,Rzwh/%ynSmu?b.hbW=<+%Hs|*0GdY>d#sVX#>3fQ4Rf/mA'

api = Api(app)


players = {
           9 : {"name": "Tanaka", "position": "forward", "age":25},
           51: {"name": "Luk", "position": "goalkeeper", "age":19},
           5 : {"name": "Quincy", "position": "defender", "age":34}
}

class PlayerList(Resource):
    def get(self):
        return players


api.add_resource(PlayerList, '/players')

@app.route('/playersForm')
def playersForm():
    return render_template('playersForm.html',  players=players)


@app.route("/", methods=["POST"])
def newPlayersForm():
    if request.method == "POST":
        newPlayer = request.form.to_dict()
        if players.__contains__(newPlayer["squadNumber"]):  # check if the squad number is not in use
            abort(403, message="Could not add player because squad number already already exists")
        players[newPlayer["squadNumber"]] = newPlayer  # add new player's data to the dictionary
        return render_template('playersForm.html',  players=players)

if __name__=="__main__":
    app.run(debug=False) # Remember to set this to False