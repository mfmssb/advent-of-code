import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    from sympy.ntheory import factorint

    return (factorint,)


@app.cell
def _(factorint):
    nums = [factorint(i) for i in range(2, 20)]
    return (nums,)


@app.cell
def _(nums):
    primes = {}

    for num in nums:
        for k in num.keys():
            if k in primes.keys():
                primes[k] = max(primes[k], num[k])
            else:
                primes[k] = num[k]
    return (primes,)


@app.cell
def _(primes):
    total = 1
    for number, exponent in primes.items():
        total *= number**exponent

    total
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
