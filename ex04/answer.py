from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def build_plot():
    left_data = [5, 7, 11, 13, 17]
    right_data = [0.1, 0.2, 0.4, 0.8, -1.6]
    x_axis = [0.0, 1.0, 2.0, 3.0, 4.0]

    fig, left_axis = plt.subplots(figsize=(8, 5))
    right_axis = left_axis.twinx()

    left_axis.plot(x_axis, left_data, color="black")
    right_axis.plot(x_axis, right_data, color="red")

    left_axis.set_title("Twin axes")
    left_axis.set_xlabel("x - axis")
    left_axis.set_ylabel("Big")
    right_axis.set_ylabel("Small")
    return fig, left_axis, right_axis


def main() -> None:
    fig, _, _ = build_plot()
    fig.tight_layout()
    fig.savefig(Path(__file__).with_name("answer.png"))


if __name__ == "__main__":
    main()
