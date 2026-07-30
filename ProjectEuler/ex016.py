import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.function
def digit_sum(n: int) -> int:
    nstr = str(n)
    return sum([int(x) for x in nstr])


@app.cell
def _():
    print(digit_sum(2**1000))
    return


if __name__ == "__main__":
    app.run()
