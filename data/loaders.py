from pathlib import Path
import pandas as pd
import streamlit as st

DATA = Path(__file__).resolve().parents[1] / "data" / "sales_daily.csv"

def clean_sales(df):
    df = df.drop_duplicates()
    df = df[df["units"] >= 0].copy()
    df["revenue"] = (df["units"] * df["unit_price"]).round(2)
    return df

@st.cache_data
def load_sales():
    df = pd.read_csv(DATA, parse_dates=["date"])
    return clean_sales(df)
