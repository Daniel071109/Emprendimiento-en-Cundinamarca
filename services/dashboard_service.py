import pandas as pd
import plotly.express as px

# ==========================================
# LEER DATASET
# ==========================================

data = pd.read_csv(

    'data/localidades.csv',

    encoding='latin1',

    sep=',',

    engine='python',

    on_bad_lines='skip'
)

# ==========================================
# LIMPIAR COLUMNAS
# ==========================================

data.columns = data.columns.str.strip()

# ==========================================
# LIMPIAR TEXTO
# ==========================================

data['NOMBRE_LOCALIDAD'] = (

    data['NOMBRE_LOCALIDAD']

    .astype(str)

    .str.encode('latin1')

    .str.decode('utf-8')
)

data['SEXO'] = (

    data['SEXO']

    .astype(str)

    .str.encode('latin1')

    .str.decode('utf-8')
)

data['GRUPOEDAD'] = (

    data['GRUPOEDAD']

    .astype(str)

    .str.encode('latin1')

    .str.decode('utf-8')
)

# ==========================================
# ELIMINAR BOGOTÁ GENERAL
# ==========================================

data = data[

    data['NOMBRE_LOCALIDAD'] != 'Bogotá'
]

# ==========================================
# LOCALIDADES
# ==========================================

localidades = data.groupby(

    'NOMBRE_LOCALIDAD'

)['POBLACION'].mean().sort_values(

    ascending=False
).head(10)

df_localidades = pd.DataFrame({

    'Localidad': localidades.index,

    'Poblacion': localidades.values
})

# ==========================================
# SEXO
# ==========================================

sexo = data.groupby(

    'SEXO'

)['POBLACION'].mean()

df_sexo = pd.DataFrame({

    'Sexo': sexo.index,

    'Poblacion': sexo.values
})

# ==========================================
# GRUPO EDAD
# ==========================================

grupo = data.groupby(

    'GRUPOEDAD'

)['POBLACION'].mean().sort_values(

    ascending=False
).head(10)

df_grupo = pd.DataFrame({

    'Grupo': grupo.index,

    'Poblacion': grupo.values
})

# ==========================================
# FUNCION DASHBOARD
# ==========================================

def obtener_dashboard():

    # ======================================
    # GRAFICA LOCALIDADES
    # ======================================

    fig_localidades = px.bar(

        df_localidades,

        x='Localidad',

        y='Poblacion',

        text='Poblacion',

        title='Top Localidades con Mayor Potencial de Emprendimiento'
    )

    fig_localidades.update_traces(

        textposition='outside'
    )

    fig_localidades.update_layout(

        paper_bgcolor='#1e293b',

        plot_bgcolor='#1e293b',

        font_color='white',

        title_x=0.5,

        height=600,

        xaxis_tickangle=-25
    )

    # ======================================
    # GRAFICA SEXO
    # ======================================

    fig_sexo = px.pie(

        df_sexo,

        values='Poblacion',

        names='Sexo',

        title='Distribución Demográfica por Sexo'
    )

    fig_sexo.update_layout(

        paper_bgcolor='#1e293b',

        font_color='white',

        title_x=0.5,

        height=500
    )

    # ======================================
    # GRAFICA EDADES
    # ======================================

    fig_grupo = px.bar(

        df_grupo,

        x='Grupo',

        y='Poblacion',

        text='Poblacion',

        title='Segmentación de Mercado por Edad'
    )

    fig_grupo.update_traces(

        textposition='outside'
    )

    fig_grupo.update_layout(

        paper_bgcolor='#1e293b',

        plot_bgcolor='#1e293b',

        font_color='white',

        title_x=0.5,

        height=600
    )

    # ======================================
    # HTML
    # ======================================

    graph_localidades = fig_localidades.to_html(

        full_html=False
    )

    graph_sexo = fig_sexo.to_html(

        full_html=False
    )

    graph_grupo = fig_grupo.to_html(

        full_html=False
    )

    # ======================================
    # KPIS
    # ======================================

    total_poblacion = int(

        data['POBLACION'].mean()

    )

    total_localidades = data[

        'NOMBRE_LOCALIDAD'

    ].nunique()

    localidad_top = df_localidades.iloc[0][

        'Localidad'
    ]

    grupo_top = df_grupo.iloc[0][

        'Grupo'
    ]

    # ======================================
    # RETORNO
    # ======================================

    return {

        'graph_localidades': graph_localidades,

        'graph_sexo': graph_sexo,

        'graph_grupo': graph_grupo,

        'total_poblacion': total_poblacion,

        'total_localidades': total_localidades,

        'localidad_top': localidad_top,

        'grupo_top': grupo_top,

        'top': df_localidades.to_dict(
            orient='records'
        )
    }