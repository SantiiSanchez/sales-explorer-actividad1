"""Activity 1 starter: a deliberately notebook-style Streamlit app.

Goal (30 min): run it, finish the TODOs, push it to GitHub and deploy it
on Streamlit Community Cloud. Everything is in ONE file on purpose:
Activity 2 refactors it into modules.

Run from the kit root:   streamlit run session1/activity1_starter/app.py

When you move this app to YOUR OWN repo: copy data/sales_daily.csv next to
app.py and change DATA to Path(__file__).parent / "sales_daily.csv".
"""
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

DATA = Path(__file__).parent / "sales_daily.csv"

st.set_page_config(page_title="Sales Explorer", layout="wide")
st.title("Sales Explorer")

df = pd.read_csv(DATA, parse_dates=["date"])

# TODO 1: Filtro de región
region = st.selectbox("Región", ["Todas"] + sorted(df["region"].unique().tolist()))

if region != "Todas":
    df = df[df["region"] == region]

# TODO 2: Filtro de categoría
categoria = st.selectbox("Categoría", ["Todas"] + sorted(df["category"].unique().tolist()))

if categoria != "Todas":
    df = df[df["category"] == categoria]

# TODO 3: Indicadores de ventas
col1, col2, col3 = st.columns(3)

col1.metric("Unidades", df["units"].sum())
col2.metric("Ingresos", f"${df['revenue'].sum():,.2f}")
col3.metric("SKUs", df["sku"].nunique())

# Primera gráfica: unidades diarias
daily = df.groupby("date", as_index=False)["units"].sum()
fig = px.line(daily, x="date", y="units", title="Unidades diarias")
st.plotly_chart(fig, width="stretch")

# TODO 4: Top 10 productos por ingresos
top10 = df.groupby("sku", as_index=False)["revenue"].sum()
top10 = top10.sort_values("revenue", ascending=False).head(10)

fig2 = px.bar(top10, x="sku", y="revenue", title="Top 10 de SKUs por ingresos")
st.plotly_chart(fig2, width="stretch")

# TODO 5: Mostrar datos filtrados (opcional)
with st.expander("Ver datos filtrados"):
    st.dataframe(df)