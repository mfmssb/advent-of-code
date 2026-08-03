import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    # Use quadratic regression to obtain diagonal formula
    def vals_NW(n):
        return 3 - 6*n + 4*n**2

    def vals_NE(n):
        return 1 - 4*n + 4*n**2

    def vals_SE(n):
        return 7 - 10*n + 4*n**2

    def vals_SW(n):
        return 5 - 8*n + 4*n**2

    return vals_NE, vals_NW, vals_SE, vals_SW


@app.cell
def _(vals_NE, vals_NW, vals_SE, vals_SW):
    def sum_diagonals(n):
        it = range(1, n+1)
        NW = [vals_NW(x) for x in it]
        NE = [vals_NE(x) for x in it]
        SE = [vals_SE(x) for x in it]
        SW = [vals_SW(x) for x in it]

        return sum(NW + NE + SE + SW) - 3

    assert sum_diagonals(3) == 101
    return (sum_diagonals,)


@app.cell
def _(sum_diagonals):
    N = 1001
    n = N // 2 + 1

    print(sum_diagonals(n))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
