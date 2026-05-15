import pandas as pd

# ==========================================
# LEER DATASETS
# ==========================================

emprendimiento = pd.read_csv(
    'data/emprendimiento.csv',
    encoding='latin1',
    sep=';'
)

localidades = pd.read_csv(
    'data/localidades.csv',
    encoding='latin1',
    sep=';'
)

mercado = pd.read_excel(
    'data/mercado.xlsx'
)

pib = pd.read_excel(
    'data/pib.xlsx'
)

dinamica = pd.read_excel(
    'data/dinamica.xlsx'
)

# ==========================================
# AGREGAR CATEGORIA
# ==========================================

emprendimiento['Categoria'] = 'Emprendimiento'

localidades['Categoria'] = 'Localidades'

mercado['Categoria'] = 'Mercado'

pib['Categoria'] = 'PIB'

dinamica['Categoria'] = 'Dinamica Economica'

# ==========================================
# UNIR DATASETS
# ==========================================

datasets = [

    emprendimiento,

    localidades,

    mercado,

    pib,

    dinamica
]

master = pd.concat(

    datasets,

    ignore_index=True,

    sort=False
)

# ==========================================
# LIMPIAR
# ==========================================

master = master.fillna('Sin dato')

# ==========================================
# GUARDAR CSV FINAL
# ==========================================

master.to_csv(

    'data/datos_maestros.csv',

    index=False,

    encoding='utf-8'
)

# ==========================================
# RESULTADO
# ==========================================

print('\nDATASET MAESTRO CREADO\n')

print(master.head())

print('\nTOTAL REGISTROS:\n')

print(len(master))