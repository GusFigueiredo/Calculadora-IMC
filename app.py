from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def site():
    altura = None
    peso = None
    imc = None
    textoImc = None
    id = None

    if request.method == "POST":
        altura = float(request.form["altura"])
        peso = float(request.form["peso"])

        imc = peso / (altura * altura)

        if imc < 18.5:
            textoImc = "Abaixo do peso"
            id = "abaixo"
        elif imc >= 18.5 and imc < 24.99:
            textoImc = "Normal"
            id = "normal"
        elif imc >= 25 and imc < 29.99:
            textoImc = "Sobrepeso"
            id = "sobrepeso"
        else:
            textoImc = "Obeso"
            id = "obeso"

    return render_template('index.html', textoImc = textoImc, imc = imc, id = id)

if __name__ == '__main__':
    app.run()