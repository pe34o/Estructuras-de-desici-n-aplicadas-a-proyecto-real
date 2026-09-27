from flask import Flask, render_template, request

app = Flask(__name__)


def estado_documentos(perfil, documentos):
    perfiles_validos = ["medical"]

    # Validar perfil
    if perfil not in perfiles_validos:
        return "data invalida"

    # Validar cantidad
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

    # Valores iniciales de los documentos
    dui = False
    antecedentes = False
    carnet = False

    if request.method == "POST":

        perfil = request.form.get("perfil")

        # Obtener los documentos marcados
        dui = request.form.get("dui") == "si"
        antecedentes = request.form.get("antecedentes") == "si"
        carnet = request.form.get("carnet") == "si"

        # Contar documentos completados
        documentos = sum([dui, antecedentes, carnet])

        # Determinar estado
        estado = estado_documentos(perfil, documentos)

    return render_template(
        "index.html",
        estado=estado,
        dui=dui,
        antecedentes=antecedentes,
        carnet=carnet
    )


if __name__ == "__main__":
    app.run(debug=True)
