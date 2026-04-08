from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def build_plot():
    fig = plt.figure(figsize=(10, 6))
    for index in range(1, 7):
        axis = fig.add_subplot(2, 3, index)
        axis.set_title(f"Title {index}")
        axis.text(
            0.5,
            0.5,
            f"(2,3,{index})",
            ha="center",
            va="center",
            transform=axis.transAxes,
        )
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    return fig


def main() -> None:
    fig = build_plot()
    fig.savefig(Path(__file__).with_name("answer.png"))


if __name__ == "__main__":
    main()
