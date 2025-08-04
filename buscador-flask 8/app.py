from flask import Flask, render_template, request
from algoritmos_busqueda import busqueda_secuencial, busqueda_binaria, generar_lista_aleatoria

app = Flask(__name__)

lista_numeros = generar_lista_aleatoria()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/busqueda_secuencial", methods=["GET", "POST"])
def busqueda_secuencial_view():
    global lista_numeros
    resultado = None
    estados = ['no'] * len(lista_numeros)
    valor_buscado = ""
    if request.method == "POST":
        if "generar" in request.form:
            lista_numeros = generar_lista_aleatoria()
            estados = ['no'] * len(lista_numeros)
        else:
            valor_buscado = request.form.get("buscado", "")
            if valor_buscado.isdigit():
                resultado, estados = busqueda_secuencial(lista_numeros, int(valor_buscado))
    return render_template(
        "busqueda_secuencial.html",
        lista=lista_numeros,
        resultado=resultado,
        estados=estados,
        buscado=valor_buscado
    )

@app.route("/busqueda_binaria", methods=["GET", "POST"])
def busqueda_binaria_view():
    global lista_numeros
    resultado = None
    pasos = ['no'] * len(lista_numeros)
    valor_buscado = ""
    lista_ordenada = sorted(lista_numeros)
    if request.method == "POST":
        if "generar" in request.form:
            lista_numeros = generar_lista_aleatoria()
            lista_ordenada = sorted(lista_numeros)
            pasos = ['no'] * len(lista_ordenada)
        else:
            valor_buscado = request.form.get("buscado", "")
            if valor_buscado.isdigit():
                resultado, pasos = busqueda_binaria(lista_ordenada, int(valor_buscado))
    return render_template(
        "busqueda_binaria.html",
        lista=lista_ordenada,
        resultado=resultado,
        pasos=pasos,
        buscado=valor_buscado
    )

if __name__ == "__main__":
    app.run(debug=True)