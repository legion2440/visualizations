import importlib


MODULES = ["pandas", "numpy", "jupyter", "matplotlib", "plotly"]


def main() -> None:
    for name in MODULES:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"{name}: OK ({version})")


if __name__ == "__main__":
    main()
