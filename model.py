import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression
import pickle

# Cargar ejemplos iniciales de textos y sus puntuaciones (pueden ser más)
data = {
    "text": [
        "Este texto tiene varios errores, por lo tanto, debería tener una puntuación baja.",
        "Este texto es algo bueno, pero tiene algunos errores.",
        "Este es un excelente texto, con apenas errores."
    ],
    "score": [30, 60, 99]  # Puntuaciones asignadas a los textos
}

# Convertir en DataFrame
df = pd.DataFrame(data)

# Vectorización de los textos usando TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])

# Crear y entrenar un modelo de regresión lineal
model = LinearRegression()
model.fit(X, df['score'])

# Guardar el modelo y el vectorizador en archivos pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Modelo entrenado y guardado.")
