"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)
@app.route('/game')
def show_madlib_form():
    """Display the madlib form"""
    response = int(request.args.get("letsplay"))

    player = request.args.get("person")

    if response:
        return render_template("game.html", person=player)
    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """prints out the funny story!!!!!!"""
    color   = request.args.get("color")
    noun    = request.args.get("noun")
    noun1   = request.args.get("noun1")
    person  = request.args.get("person")
    person1 = request.args.get("person1")
    adverb  = request.args.get("adverb")
    bodypart    = request.args.get("bodypart")
    rightleft   = request.args.get("rightleft")
    pastverb    = request.args.get("pastverb")
    adjective   = request.args.get("adjective")

    return render_template("madlib.html", color=color, noun=noun, noun1=noun1, person=person, person1=person1, adverb=adverb, rightleft=rightleft, bodypart=bodypart,pastverb=pastverb, adjective=adjective)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
