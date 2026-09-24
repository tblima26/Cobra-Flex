from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/melhorCombustivel",methods=['POST'])
def calcular_combustivel():
    gasolina = None
    etanol = None
    result = None
    msg = None
    if request.method == 'POST':
        gasolina = float(request.form.get("gasolina","").replace(",","."))
        etanol = float(request.form.get("etanol","").replace(",","."))
        result = "Etanol" if etanol <= gasolina*0.75 else "Gasolina"
        msg = f"Melhor abastecer com {result}."
    return render_template("index.html", msg=msg)


if __name__ == "__main__":
    app.run(debug=True)