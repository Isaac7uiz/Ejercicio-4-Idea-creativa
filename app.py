from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        modelo = request.form['modelo']
        serial = request.form['serial']
        return redirect(url_for('confirmacion', nombre=nombre, modelo=modelo, serial=serial))
    return render_template('registro.html')

@app.route('/confirmacion')
def confirmacion():
    nombre = request.args.get('nombre')
    modelo = request.args.get('modelo')
    serial = request.args.get('serial')
    return render_template('confirmacion.html', nombre=nombre, modelo=modelo, serial=serial)

if __name__ == '__main__':
    app.run(debug=True)
