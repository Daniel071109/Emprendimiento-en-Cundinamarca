def entrenar_kmeans():
    """Retorna datos de ejemplo para K-Means - SIN Spark"""
    
    clusters = [
        {"id": 1, "localidad": "Suba", "poblacion": 5730, "empresas": 12500, "tasa": 92.5, "cluster": 0},
        {"id": 2, "localidad": "Kennedy", "poblacion": 5163, "empresas": 11200, "tasa": 91.8, "cluster": 0},
        {"id": 3, "localidad": "Engativá", "poblacion": 3977, "empresas": 8600, "tasa": 89.2, "cluster": 0},
        {"id": 4, "localidad": "Bosa", "poblacion": 3481, "empresas": 7500, "tasa": 88.4, "cluster": 1},
        {"id": 5, "localidad": "Ciudad Bolívar", "poblacion": 3192, "empresas": 6900, "tasa": 87.6, "cluster": 1},
        {"id": 6, "localidad": "Usaquén", "poblacion": 2653, "empresas": 5700, "tasa": 86.0, "cluster": 1},
        {"id": 7, "localidad": "San Cristóbal", "poblacion": 1927, "empresas": 4200, "tasa": 84.0, "cluster": 2},
        {"id": 8, "localidad": "Usme", "poblacion": 1840, "empresas": 4000, "tasa": 83.5, "cluster": 2},
        {"id": 9, "localidad": "Rafael Uribe", "poblacion": 1817, "empresas": 3950, "tasa": 83.2, "cluster": 2},
        {"id": 10, "localidad": "Fontibón", "poblacion": 1786, "empresas": 3880, "tasa": 83.0, "cluster": 2}
    ]
    
    centros = [
        {"cluster": 0, "poblacion": 4956.67, "empresas": 10766.67, "tasa": 91.17},
        {"cluster": 1, "poblacion": 3108.67, "empresas": 6700.00, "tasa": 87.33},
        {"cluster": 2, "poblacion": 1842.50, "empresas": 4007.50, "tasa": 83.43}
    ]
    
    # Datos para el gráfico de clusters
    grafico_datos = {
        "localidades": [item["localidad"] for item in clusters],
        "poblaciones": [item["poblacion"] for item in clusters],
        "empresas": [item["empresas"] for item in clusters],
        "tasas": [item["tasa"] for item in clusters],
        "clusters": [item["cluster"] for item in clusters]
    }
    
    return {
        "error": None,
        "silhouette_score": 0.7245,
        "clusters": clusters,
        "centros": centros,
        "grafico_datos": grafico_datos
    }