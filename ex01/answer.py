from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import pandas as pd


def build_plot():
    df = pd.DataFrame(
        {
            "name": ["christopher", "marion", "maria", "mia", "clement", "randy", "remi"],
            "age": [70, 30, 22, 19, 45, 33, 20],
            "gender": ["M", "F", "F", "F", "M", "M", "M"],
            "state": ["california", "dc", "california", "dc", "california", "new york", "porto"],
            "num_children": [4, 2, 1, 0, 3, 1, 0],
            "num_pets": [5, 1, 0, 2, 2, 2, 3],
        }
    )
    ax = df.plot.bar(x="name", y="age", figsize=(8, 5), rot=90)
    ax.set_title("Age per name")
    ax.set_xlabel("name")
    ax.set_ylabel("")
    ax.legend()
    return ax.figure, ax


def main() -> None:
    fig, _ = build_plot()
    fig.tight_layout()
    fig.savefig(Path(__file__).with_name("answer.png"))


if __name__ == "__main__":
    main()
