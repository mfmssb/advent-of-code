import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.function
def sum_of_squares(l: list) -> int:
    s = 0
    for x in l:
        s += x**2
    return s


@app.function
def square_sum(l: list) -> int:
    return sum(l)**2


@app.function
def diff_of_squares(n: int) -> int:
    l = [i for i in range(n + 1)]
    return square_sum(l) - sum_of_squares(l)


@app.cell
def _():
    diff_of_squares(100)
    return


if __name__ == "__main__":
    app.run()
