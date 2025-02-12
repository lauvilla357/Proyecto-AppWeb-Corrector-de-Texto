# Proyecto-AppWeb-Corrector-de-Texto

## Corrector de Texto

Este proyecto es una aplicación web que permite corregir y puntuar textos de forma automática, utilizando un modelo de aprendizaje automático simple integrado en una aplicación web. El objetivo es mostrar cómo se puede integrar un modelo sencillo en una web para visualizar la predicción de puntuaciones de textos.

### Descripción

La aplicación utiliza un modelo de regresión lineal entrenado con un dataframe simple de solo tres textos. Este modelo se utiliza para predecir la puntuación de un texto, basado en su calidad. Aunque el modelo es básico, el propósito principal es demostrar la integración de modelos de Machine Learning en una aplicación web utilizando Flask.

### Características principales:

- Modelo simple: Entrenado con solo tres textos y sus puntuaciones.
- Interfaz sencilla: Permite al usuario ingresar un texto y obtener una puntuación.
- Backend en Flask: El modelo se ejecuta en el servidor Flask, haciendo la aplicación interactiva.
- Visualización web: La puntuación es mostrada en la interfaz web en tiempo real.

### Tecnologías Utilizadas

- Flask: Framework web para crear aplicaciones web ligeras y rápidas.
- Scikit-learn: Biblioteca de Python para el aprendizaje automático, utilizada para entrenar el modelo de regresión lineal.
- TF-IDF: Técnica de vectorización de texto usada para transformar los textos en vectores numéricos.
- HTML, CSS: Para la estructura y diseño de la interfaz de usuario.
- JavaScript: Para la interactividad en el frontend.

### Instalación y Ejecución

1. **Clona el repositorio**:

   Abre tu terminal y ejecuta el siguiente comando para clonar el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/corrector-texto.git
   cd corrector-texto
   
2. **Crea y activa el entorno virtual**:

   Para Windows:

   ```bash
   python -m venv entorno1
   .\entorno1\Scripts\activate

3. **Ejecuta la aplicación**:

   ```bash
   python app.py

  Ahora la aplicación debería estar disponible en la siguiente URL en tu navegador: http://127.0.0.1:5000/

### Muestrario de imágenes

Se provee una carpeta bajo el nombre de "imagenes" para proporcionar una muestra de la aplicación y el aspecto de la interfaz.
