import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    from sympy import proper_divisors
    import pandas as pd
    import numpy as np

    return np, proper_divisors


@app.cell
def _(proper_divisors):
    UPPERBOUND = 28124
    abundants = [i for i in range(UPPERBOUND+1) if i < sum(proper_divisors(i))]
    return UPPERBOUND, abundants


@app.cell
def _(UPPERBOUND, abundants, np):
    grid = np.add.outer(abundants, abundants)
    values = np.unique(grid)
    values = values[values <= UPPERBOUND]
    return (values,)


@app.cell
def _(UPPERBOUND, values):
    sum(set(range(1, UPPERBOUND)) - set(values))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
