import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    from math import gcd
    from functools import reduce
    from sympy import factorint


    def canonical_power(a: int, b: int) -> tuple[int, int]:
        factors = factorint(a)
        common = reduce(gcd, factors.values())

        base = 1
        for prime, exponent in factors.items():
            base *= prime ** (exponent // common)
 
        return base, common * b


    n = 100

    distinct = {
        canonical_power(a, b)
        for a in range(2, n + 1)
        for b in range(2, n + 1)
    }

    len(distinct)
    return


if __name__ == "__main__":
    app.run()
