from bottle import route, run, template
from helpers import somme


@route("/add/<x>/<y>")
def add(x, y):
    resultat = somme(x, y)
    return template(
        "<b>La somme de {{x}} et {{y}} est {{resultat}}</b>!",
        x=x,
        y=y,
        resultat=resultat,
    )


run(host="localhost", port=8089)
