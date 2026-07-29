import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    from sympy.ntheory import isprime

    return (isprime,)


@app.cell
def _(isprime):
    s = 0
    for num in range(2*10**6 + 1):
        if isprime(num):
            s += num
    s
    return


if __name__ == "__main__":
    app.run()
