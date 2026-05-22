from flask import Flask, render_template

from services.dashboard_service import obtener_dashboard

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

    return render_template(

        'dashboard.html',

        graph_localidades=data['graph_localidades'],

        graph_sexo=data['graph_sexo'],

        graph_grupo=data['graph_grupo'],

        total_poblacion=data['total_poblacion'],

        total_localidades=data['total_localidades'],

        localidad_top=data['localidad_top'],

        grupo_top=data['grupo_top'],

        top=data['top']
    )

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
# ABOUT
# ==========================================

@app.route('/about')
def about():

    return render_template('about.html')

# ==========================================
# ==========================================
# BUSINESS ANALYTICS
# ==========================================

@app.route('/business-analytics')
def business_analytics():
    return render_template('business_analytics.html')

# ==========================================
# PYSPARK ANALYTICS
# ==========================================

from services.spark import obtener_resultados

@app.route('/pyspark-analisis')
def pyspark_analisis():
    resultados = obtener_resultados()
    return render_template('pyspark_analisis.html', **resultados)

if __name__ == '__main__':

    app.run(

        host='0.0.0.0',

        port=5000,

        debug=True
    )