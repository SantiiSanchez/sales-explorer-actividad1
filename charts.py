import plotly.express as px

def daily_units_chart(df):
    diario = df.groupby("date", as_index=False)["units"].sum()
    return px.line(diario, x="date", y="units", title="Unidades diarias")

def top_skus_chart(df):
    top10 = df.groupby("sku", as_index=False)["revenue"].sum()
    top10 = top10.sort_values("revenue", ascending=False).head(10)
    return px.bar(top10, x="sku", y="revenue", title="Top 10 de SKUs por ingresos")
