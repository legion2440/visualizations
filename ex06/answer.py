from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def build_dataframe():
    np.random.seed(0)
    returns = np.random.randn(50)
    price = 100 + np.cumsum(returns)
    dates = pd.date_range(start="2020-09-01", periods=50, freq="B")
    return pd.DataFrame(zip(dates, price), columns=["Date", "Company_A"])


def build_express_figure(df=None):
    if df is None:
        df = build_dataframe()
    fig = px.line(df, x="Date", y="Company_A", title="Company A Price")
    fig.update_layout(xaxis_title="Date", yaxis_title="Price")
    return fig


def build_graph_objects_figure(df=None):
    if df is None:
        df = build_dataframe()
    fig = go.Figure(
        data=[
            go.Scatter(
                x=df["Date"],
                y=df["Company_A"],
                mode="lines",
                name="Company_A",
            )
        ]
    )
    fig.update_layout(title="Company A Price", xaxis_title="Date", yaxis_title="Price")
    return fig


def main() -> None:
    df = build_dataframe()
    build_express_figure(df).write_html(Path(__file__).with_name("express.html"))
    build_graph_objects_figure(df).write_html(Path(__file__).with_name("graph_objects.html"))


if __name__ == "__main__":
    main()
