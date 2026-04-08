from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import pandas as pd


def build_plot():
    df = pd.DataFrame(
        {
            "Age": [18, 22, 27, 31, 36, 42, 47, 53, 58],
            "Children": [0, 0, 1, 1, 2, 2, 3, 4, 5],
        }
    )
    ax = df.plot.scatter(x="Age", y="Children", figsize=(8, 5), color="tab:blue")
    ax.set_title("Age vs Number of Children")
    ax.set_xlabel("Age")
    ax.set_ylabel("Children")
    return ax.figure, ax


def main() -> None:
    fig, _ = build_plot()
    fig.tight_layout()
    fig.savefig(Path(__file__).with_name("answer.png"))


if __name__ == "__main__":
    main()
