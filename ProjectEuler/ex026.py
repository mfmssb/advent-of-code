import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    from sympy import n_order
    from math import gcd

    return gcd, n_order


@app.cell
def _(gcd, n_order):
    def period_length(a: int, d: int) -> int:
        if d == 0:
            raise ZeroDivisionError

        d = abs(d) // gcd(a, d)

        while d % 2 == 0:
            d //= 2

        while d % 5 == 0:
            d //= 5

        return 0 if d == 1 else int(n_order(10, d))


    def decimal_period(a: int, d: int) -> str:
        if d == 0:
            raise ZeroDivisionError("Nevneren kan ikke være 0")

        a = abs(a)
        d = abs(d)

        remainder = a % d

        seen_remainders = {}
        digits = []

        while remainder != 0:
            if remainder in seen_remainders:
                period_start = seen_remainders[remainder]
                return "".join(digits[period_start:])

            seen_remainders[remainder] = len(digits)

            remainder *= 10
            digit, remainder = divmod(remainder, d)
            digits.append(str(digit))

        return ""

    return decimal_period, period_length


@app.cell
def _(decimal_period, period_length):
    N = 1000
    data = {
        "n": list(range(1, N + 1)),
        "1_div_n": [1 / i for i in range(1, N + 1)],
        "period_len": [period_length(1, i) for i in range(1, N + 1)],
        "period": [decimal_period(1, i) for i in range(1, N + 1)],
    }
    return (data,)


@app.cell
def _():
    import pandas as pd

    return (pd,)


@app.cell
def _(data, pd):
    df = pd.DataFrame(data)
    return (df,)


@app.cell
def _(df):
    df
    return


if __name__ == "__main__":
    app.run()
