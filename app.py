from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/senha")
def senha():
    return render_template("senha.html")


@app.route("/confirmacao")
def confirmacao():
    return render_template("confirmacao.html")


@app.route("/sem-confirmar")
def sem_confirmar():
    return render_template("erro404.html"), 404


@app.route("/final")
def final():
    return render_template("final.html")


if __name__ == "__main__":
    app.run(debug=True)