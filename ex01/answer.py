from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import pandas as pd


def build_plot():
    df = pd.DataFrame(
        {
            "Math": [72, 75, 78, 80],
            "Science": [68, 73, 77, 82],
        },
        index=["Class A", "Class B", "Class C", "Class D"],
    )
    ax = df.plot(kind="bar", figsize=(8, 5))
    ax.set_title("Scores by Class")
    ax.set_xlabel("Class")
    ax.set_ylabel("Score")
    ax.legend(title="Subject")
    return ax.figure, ax


def main() -> None:
    fig, _ = build_plot()
    fig.tight_layout()
    fig.savefig(Path(__file__).with_name("answer.png"))


if __name__ == "__main__":
    main()
