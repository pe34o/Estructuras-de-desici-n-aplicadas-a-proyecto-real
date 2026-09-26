from flask import Flask, request

app = Flask(__name__)

@app.route("/documentos")
def documentos():
    dui = request.args.get("dui") == "si"
    antecedentes = request.args.get("antecedentes") == "si"
    carnet = request.args.get("carnet") == "si"

    nombres_documentos = ["DUI", "Antecedentes", "Carnet de junta"]
    estados_documentos = [dui, antecedentes, carnet]

    contador = 0
    filas_html = ""
    for i in range(len(estados_documentos)):
        if estados_documentos[i]:
            contador += 1
            icono = "check"
        else:
            icono = "pendiente"
        filas_html += f"<li>[{icono}] {nombres_documentos[i]}</li>"

    return f"\n    <h2>Checklist de expediente</h2>\n    <ul>{filas_html}</ul>\n    <p>Documentos completos: {contador} de {len(estados_documentos)}</p>\n    "

if __name__ == "__main__":
    app.run(debug=True)