from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def build_plot():
    x_values = [1, 4, 5, 6, 7]
    y_values = [2, 6, 3, 6, 3]

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
    ax.set_title("Display marker")
    ax.set_xlabel("x - axis")
    ax.set_ylabel("y - axis")
    ax.set_xlim([1, 8])
    ax.set_ylim([1, 8])
    return fig, ax


def main() -> None:
    fig, _ = build_plot()
    fig.tight_layout()
    fig.savefig(Path(__file__).with_name("answer.png"))


if __name__ == "__main__":
    main()
