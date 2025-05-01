from flask import Flask, render_template, request
from operacion import separar, numeros, operar

app = Flask(__name__)

saludo = "Bienvenido a la calculadora realizada con Flask  en python"
@app.route('/')
def index():
    return render_template('index.html', saludo=saludo)

@app.route('/calculadora' , methods=['GET', 'POST'])
def calculadora():
    operacion = request.form.get('pantalla')
    bloques = separar (operacion)
    transformar = numeros (bloques)
    resultado = operar (transformar)
    print (resultado)
    return render_template(
        'calculadora.html',
        bloques=bloques,  
        transformar=transformar, 
        resultado=resultado
        ) 




if __name__ == '_main_':
    app.run(debug=True)