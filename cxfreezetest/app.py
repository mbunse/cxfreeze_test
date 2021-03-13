import pandas as pd


def main():
    """
    Start and run the gui. This function is made available as a script 'keudk-gui' from the command line.
    """
    df = pd.DataFrame({"x1": [1.2, 3.0, 23.1], "x2": [4.1, 2.9, 3.7]})

    df["x3"] = df["x1"] ** 2

    print(df)


if __name__ == "__main__":
    main()
