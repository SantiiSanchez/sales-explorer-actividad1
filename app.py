
import streamlit as st

from data.loaders import load_sales
from components.charts import daily_units_chart, top_skus_chart

st.set_page_config(page_title="Sales Explorer", layout="wide")
st.title("Sales Explorer")

df = load_sales()

# 1. Filtros
regiones = sorted(df["region"].unique())
categorias = sorted(df["category"].unique())

regiones_elegidas = st.sidebar.multiselect(
    "Regiones", regiones, default=regiones, key="regiones"
)

categorias_elegidas = st.sidebar.multiselect(
    "Categorías", categorias, default=categorias, key="categorias"
)

filtrado = df[
    df["region"].isin(regiones_elegidas)
    & df["category"].isin(categorias_elegidas)
]

# 2. Selección vacía
if filtrado.empty:
    st.warning("Selecciona al menos una región y una categoría.")
    st.stop()

# 3. Indicadores
col1, col2, col3 = st.columns(3)

col1.metric("Unidades", f"{filtrado['units'].sum():,}")
col2.metric("Ingresos", f"${filtrado['revenue'].sum():,.2f}")
col3.metric("SKUs", filtrado["sku"].nunique())

# 4. Gráficas
st.plotly_chart(daily_units_chart(filtrado), width="stretch")
st.plotly_chart(top_skus_chart(filtrado), width="stretch")

# 5. Tabla de datos
with st.expander("Ver datos filtrados"):
    st.dataframe(filtrado)
