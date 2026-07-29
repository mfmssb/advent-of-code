import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import math

    return (math,)


@app.cell
def _(math):
    p = 600851475143
    proot = math.floor(math.sqrt(p))
    return p, proot


@app.cell
def _(proot):
    proot
    return


@app.cell
def _(proot):
    def divisors_of(n: int) -> list:
        divisors = []
        for i in range(2, proot+1):
            if n % i == 0:
                divisors.append(i)
        return divisors

    return (divisors_of,)


@app.cell
def _(divisors_of, p):
    d_of_p = divisors_of(p)
    d_of_p
    return (d_of_p,)


@app.cell
def _(d_of_p, divisors_of):
    is_prime = []
    for n in d_of_p:
        n_divisors = divisors_of(n)
        print(n)
        print(n_divisors)
        if len(n_divisors) == 1:
            is_prime.append(n)
    is_prime
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
