import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    from sympy.utilities.iterables import multiset_permutations
    import numpy as np
    import pandas as pd

    return multiset_permutations, pd


@app.cell
def _(multiset_permutations, pd):
    values = [str(i) for i in range(10)]
    test = [("").join(x) for x in multiset_permutations(values)]
    df = pd.DataFrame(test, columns=["perm"])
    return (df,)


@app.cell
def _(df):
    df.iloc[10**6+1]
    return


@app.cell
def _(df):
    df.iloc[10**6]
    return


if __name__ == "__main__":
    app.run()
