from flask import Flask, render_template, request, flash
from game import Game_glo
from project.forms import Choice_of_direction, Number_steps
from config import Config

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/', methods=['GET'])
def index():
    game = Game_glo()
    if request.method == "GET":
        game.reboot()
    return render_template('index.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    game = Game_glo()
    form = Choice_of_direction()
    steps = Number_steps()
    if request.method == 'POST':
        phrases = game.move(form.way.data, steps.data['steps'])
        for phrase in phrases:
            flash(phrase)
        if game.check_end_game():
            game.reboot()
        return render_template('game.html', form=form, steps=steps, game=game, phrases=phrases)
    return render_template('game.html', form=form, steps=steps, game=game)


if __name__ == '__main__':
    app.run(port=5002)
