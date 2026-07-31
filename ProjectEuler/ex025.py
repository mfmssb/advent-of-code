import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.function
def next_fib(current_fibs: list) -> list:
    f2 = current_fibs[-2]
    f1 = current_fibs[-1]
    return current_fibs + [f1 + f2]


@app.cell
def _():
    fib = [1, 1]
    while True:
        fib = next_fib(fib)
        if len(str(fib[-1])) >= 1_000:
            break
    return (fib,)


@app.cell
def _(fib):
    len(fib)
    return


@app.cell
def _(fib):
    len(str(fib[4781]))
    return


if __name__ == "__main__":
    app.run()
