from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def inicio():
    resultado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        poblacion = int(request.form['poblacion'])
        if poblacion >= 5000:
            resultado = f"Hola {nombre}, tu ciudad es grande. Tiene {poblacion} habitantes."
        else:
            resultado = f"Hola {nombre}, tu ciudad es pequeña. Tiene {poblacion} habitantes."
    return render_template('index.html', respuesta=resultado)

if __name__ == '__main__':
    app.run(debug=True)