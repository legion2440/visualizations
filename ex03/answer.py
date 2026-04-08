from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def build_plot():
    x_values = np.arange(1, 9)
    y_values = np.array([1, 3, 2, 5, 4, 7, 6, 8])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        x_values,
        y_values,
        color="red",
        linestyle="-.",
        linewidth=3,
        marker="o",
        markersize=12,
        markerfacecolor="blue",
        markeredgecolor="blue",
    )
    ax.set_title("Styled Line Plot")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_xlim([1, 8])
    ax.set_ylim([1, 8])
    return fig, ax


def main() -> None:
    fig, _ = build_plot()
    fig.tight_layout()
    fig.savefig(Path(__file__).with_name("answer.png"))


if __name__ == "__main__":
    main()
