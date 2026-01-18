import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Configuración de la página
st.set_page_config(page_title="FísicApp Pro", page_icon="🚀")

st.title("🚀 Simulador de Tiro Parabólico")
st.markdown("""
Esta herramienta ayuda a estudiantes de ingeniería a visualizar el movimiento de proyectiles.
**Cambia los valores en la barra lateral** para ver cómo afecta la trayectoria.
""")

# 2. Barra Lateral (Inputs del Usuario)
st.sidebar.header("Parámetros de Entrada")
v0 = st.sidebar.slider("Velocidad Inicial (v0) [m/s]", 5.0, 100.0, 25.0)
angulo = st.sidebar.slider("Ángulo de Lanzamiento (θ) [grados]", 10.0, 90.0, 45.0)
g = st.sidebar.number_input("Gravedad (g) [m/s²]", value=9.81)

# 3. Cálculos Físicos (La magia de la ingeniería)
theta_rad = np.radians(angulo)
t_vuelo = 2 * v0 * np.sin(theta_rad) / g
x_max = v0 * np.cos(theta_rad) * t_vuelo
y_max = (v0 * np.sin(theta_rad))**2 / (2 * g)

# Generar puntos para la gráfica
t = np.linspace(0, t_vuelo, num=100)
x = v0 * np.cos(theta_rad) * t
y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2

# 4. Mostrar Resultados Numéricos
col1, col2, col3 = st.columns(3)
col1.metric("Tiempo de Vuelo", f"{t_vuelo:.2f} s")
col2.metric("Alcance Máximo (X)", f"{x_max:.2f} m")
col3.metric("Altura Máxima (Y)", f"{y_max:.2f} m")

# 5. Gráfica Interactiva
fig, ax = plt.subplots()
ax.plot(x, y, label='Trayectoria')
ax.set_xlabel('Distancia (m)')
ax.set_ylabel('Altura (m)')
ax.set_title(f'Trayectoria con v0={v0} m/s y θ={angulo}°')
ax.grid(True, linestyle='--', alpha=0.6)
ax.axhline(0, color='black', linewidth=1)
st.pyplot(fig)

# 6. (Opcional) Tabla de datos para descargar
if st.checkbox("Ver tabla de datos detallada"):
    df = pd.DataFrame({'Tiempo (s)': t, 'X (m)': x, 'Y (m)': y})
    st.dataframe(df)