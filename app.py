from flask import Flask, render_template
from services.dashboard_service import obtener_dashboard
from services.spark import obtener_resultados, comparar_tiempos_procesamiento
from services.spark_ml import entrenar_kmeans

app = Flask(__name__)

# ==========================================
# INICIO
# ==========================================
@app.route('/')
def inicio():
    return render_template('index.html')

# ==========================================
# DASHBOARD
# ==========================================
@app.route('/dashboard')
def dashboard():
    data = obtener_dashboard()
    return render_template('dashboard.html', **data)

# ==========================================
# DATASETS
# ==========================================
@app.route('/datasets')
def datasets():
    return render_template('datasets.html')

# ==========================================
# MODELO
# ==========================================
@app.route('/modelo')
def modelo():
    return render_template('modelo.html')

# ==========================================
# BUSINESS ANALYTICS
# ==========================================
@app.route('/business-analytics')
def business_analytics():
    return render_template('business_analytics.html')

# ==========================================
# PYSPARK ANALISIS
# ==========================================
@app.route('/pyspark-analisis')
def pyspark_analisis():
    resultados = obtener_resultados()
    return render_template('pyspark_analisis.html', **resultados)

# ==========================================
# ML & TIEMPOS (K-MEANS)
# ==========================================
@app.route('/spark-ml')
def spark_ml():
    comparacion_tiempos = comparar_tiempos_procesamiento()
    kmeans_resultado = entrenar_kmeans()
    return render_template('spark_ml.html', 
                         comparacion_tiempos=comparacion_tiempos,
                         kmeans_resultado=kmeans_resultado)

# ==========================================
# CONOCIMIENTO
# ==========================================
@app.route('/conocimiento')
def conocimiento():
    return render_template('conocimiento.html')

# ==========================================
# ABOUT
# ==========================================
@app.route('/about')
def about():
    return render_template('about.html')

# ==========================================
# EJECUCION
# ==========================================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)