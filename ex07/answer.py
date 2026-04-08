from pathlib import Path

import numpy as np
import plotly.graph_objects as go


def build_plot():
    np.random.seed(0)
    y0 = np.random.randn(50)
    y1 = np.random.randn(50) + 1
    y2 = np.random.randn(50) + 2

    fig = go.Figure()
    fig.add_trace(go.Box(y=y0, name="Sample A", marker_color="#636EFA"))
    fig.add_trace(go.Box(y=y1, name="Sample B", marker_color="#EF553B"))
    fig.add_trace(go.Box(y=y2, name="Sample C", marker_color="#00CC96"))
    fig.update_layout(title="Box plot", showlegend=True)
    return fig


def main() -> None:
    fig = build_plot()
    fig.write_html(Path(__file__).with_name("answer.html"))


if __name__ == "__main__":
    main()
