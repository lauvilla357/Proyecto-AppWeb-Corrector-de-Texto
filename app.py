from flask import Flask, render_template, request, jsonify
import pickle

# Cargar el modelo y el vectorizador
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grade', methods=['POST'])
def grade_text():
    # Obtener el texto del formulario
    input_text = request.form['text']
    #print("Texto recibido:", input_text)   
    
    # Transformar el texto usando el vectorizador
    input_vector = vectorizer.transform([input_text])
    
    # Predecir la puntuación con el modelo entrenado
    score = model.predict(input_vector)[0]
    
    # Devolver el resultado
    return jsonify({'score': round(score, 2)})

if __name__ == '__main__':
    app.run(debug=True)
