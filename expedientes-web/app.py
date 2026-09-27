from flask import Flask, render_template, request
app = Flask(__name__)
PROFILE_CHECKLIST = {
    "medical": 6,
    "administrative": 4
}
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        profile = request.form.get("profile")
        cantidad_raw = request.form.get("documents_uploaded")
        try:
            cantidad = int(cantidad_raw)
        except (TypeError, ValueError):
            cantidad = None
        if profile not in PROFILE_CHECKLIST or cantidad is None or cantidad < 0:
            estado = "invalid_data"
        else:
            requeridos = PROFILE_CHECKLIST[profile]
            if cantidad == 0:
                estado = "not_started"
            elif cantidad < requeridos:
                estado = "incomplete"
            elif cantidad == requeridos:
                estado = "complete"
            else:
                estado = "over_completed"
        resultado = {
            "profile": profile,
            "documents_uploaded": cantidad,
            "status": estado,
            "signature": "# Verificado por sistema Key-2026"
        }
    return render_template("index.html", resultado=resultado)
if __name__ == "__main__":
    app.run(debug=True)
