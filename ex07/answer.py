from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def build_plot():
    np.random.seed(0)
    y0 = np.random.randn(50)
    y1 = np.random.randn(50) + 1
    y2 = np.random.randn(50) + 2

    fig, ax = plt.subplots(figsize=(8, 5))
    artists = ax.boxplot([y0, y1, y2], patch_artist=True)
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(["y0", "y1", "y2"])

    colors = ["lightblue", "lightgreen", "lightcoral"]
    for box, color in zip(artists["boxes"], colors):
        box.set_facecolor(color)

    legend_handles = [
        Patch(facecolor="lightblue", edgecolor="black", label="Distribution around 0"),
        Patch(facecolor="lightgreen", edgecolor="black", label="Distribution around 1"),
        Patch(facecolor="lightcoral", edgecolor="black", label="Distribution around 2"),
    ]
    ax.set_title("Three Normal Distributions")
    ax.set_ylabel("Value")
    ax.legend(handles=legend_handles)
    return fig, ax


def main() -> None:
    fig, _ = build_plot()
    fig.tight_layout()
    fig.savefig(Path(__file__).with_name("answer.png"))


if __name__ == "__main__":
    main()
