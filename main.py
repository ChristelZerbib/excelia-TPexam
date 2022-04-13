from bottle import route, run, template
from helpers import somme
import sys


@route("/add/<x>/<y>")
def add(x, y):
    resultat = somme(x, y)
    return template(
        "<b>La somme de {{x}} et {{y}} est {{resultat}}</b>, même sur dev !",
        x=x,
        y=y,
        resultat=resultat,
    )


run(host="0.0.0.0", port=sys.argv[1], reloader=True)
