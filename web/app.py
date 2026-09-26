from flask import Flask, render_template, request

app = Flask(__name__)


def estado_documentos(perfil, documentos):

    perfiles_validos = ["medical"]

    if perfil not in perfiles_validos:
        return "data invalida"

    if documentos < 0:
        return "data invalida"

    if documentos == 0:
        return "no comenzado"

    elif documentos < 3:
        return "incompleto"

    elif documentos == 3:
        return "completo"

    else:
        return "cantidad de archivos excedida"


@app.route("/", methods=["GET", "POST"])
def inicio():

    estado = None

    if request.method == "POST":

        perfil = request.form["perfil"]

        try:
            documentos = int(request.form["documentos"])
            estado = estado_documentos(perfil, documentos)

        except ValueError:
            estado = "data invalida"

    return render_template("index.html", estado=estado)


if __name__ == "__main__":
    app.run(debug=True)