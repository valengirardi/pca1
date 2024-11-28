import streamlit as st
import plotly.graph_objects as go

# Aquí va tu código para generar el gráfico 'fig'
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
import plotly.graph_objects as go

# Cargar los datos desde un archivo Excel
file_path = "PCA.xlsx"  # Asegúrate de cargar este archivo en tu repositorio
data = pd.read_excel(file_path)

# Establecer 'sample-id' como el índice del DataFrame
data.set_index('sample-id', inplace=True)

# Escalar los datos numéricos
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Aplicar PCA para reducir a 3 componentes principales
pca = PCA(n_components=3)
projected_data = pca.fit_transform(scaled_data)

# Convertir los datos proyectados a un DataFrame
projected_df = pd.DataFrame(data=projected_data, columns=[f'PC{i}' for i in range(1, 4)])
projected_df['type-of-reactor'] = data.index

# Crear un objeto go.Figure
fig = go.Figure()

# Añadir los puntos al gráfico
fig.add_trace(go.Scatter3d(
    x=projected_df['PC1'],
    y=projected_df['PC2'],
    z=projected_df['PC3'],
    mode='markers+text',
    marker=dict(size=4, color=projected_df['PC1'], opacity=0.8),
    text=projected_df['type-of-reactor'],
    textposition='top center',
    textfont=dict(size=8),
    name='Samples'
))

# Mostrar el gráfico en Streamlit
st.title("Gráfico PCA Interactivo")
st.plotly_chart(fig)
