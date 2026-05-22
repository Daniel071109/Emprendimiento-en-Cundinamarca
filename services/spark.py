import os
import sys

def obtener_resultados():
    """Retorna datos de ejemplo para PySpark - SIN Spark"""
    
    # Datos fijos de localidades
    top_localidades = [
        {"LOCALIDAD": "Suba", "poblacion_promedio": 5730},
        {"LOCALIDAD": "Kennedy", "poblacion_promedio": 5163},
        {"LOCALIDAD": "Engativá", "poblacion_promedio": 3977},
        {"LOCALIDAD": "Bosa", "poblacion_promedio": 3481},
        {"LOCALIDAD": "Ciudad Bolívar", "poblacion_promedio": 3192},
        {"LOCALIDAD": "Usaquén", "poblacion_promedio": 2653},
        {"LOCALIDAD": "San Cristóbal", "poblacion_promedio": 1927},
        {"LOCALIDAD": "Usme", "poblacion_promedio": 1840},
        {"LOCALIDAD": "Rafael Uribe Uribe", "poblacion_promedio": 1817},
        {"LOCALIDAD": "Fontibón", "poblacion_promedio": 1786}
    ]
    
    distribucion_sexo = [
        {"SEXO": "Femenino", "poblacion_promedio": 1927, "cantidad_registros": 62620},
        {"SEXO": "Masculino", "poblacion_promedio": 1797, "cantidad_registros": 62620}
    ]
    
    distribucion_edad = [
        {"GRUPO_EDAD": "18 a 28", "poblacion_promedio": 3184, "cantidad_registros": 13640},
        {"GRUPO_EDAD": "12 a 17", "poblacion_promedio": 2788, "cantidad_registros": 7440},
        {"GRUPO_EDAD": "29 a 59", "poblacion_promedio": 2624, "cantidad_registros": 38440},
        {"GRUPO_EDAD": "00 a 11", "poblacion_promedio": 2437, "cantidad_registros": 14880},
        {"GRUPO_EDAD": "60 o más", "poblacion_promedio": 629, "cantidad_registros": 50840}
    ]
    
    resumen_general = [{
        "total_localidades": 20,
        "total_registros": 125240,
        "poblacion_promedio_general": 1862
    }]
    
    return {
        "top_localidades": top_localidades,
        "distribucion_sexo": distribucion_sexo,
        "distribucion_edad": distribucion_edad,
        "resumen_general": resumen_general,
        "tasa_ocupacion": 32.2,
        "modo": "Datos de ejemplo"
    }

def comparar_tiempos_procesamiento():
    """Retorna datos de ejemplo para comparación de tiempos"""
    return [
        {"configuracion": "Local (sin workers)", "master": "local", "workers": 0, "tiempo_segundos": 2.45},
        {"configuracion": "Master + 1 worker", "master": "local[1]", "workers": 1, "tiempo_segundos": 1.82},
        {"configuracion": "Master + 2 workers", "master": "local[2]", "workers": 2, "tiempo_segundos": 1.34}
    ]