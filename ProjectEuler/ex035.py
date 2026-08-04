import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    from itertools import permutations
    from sympy import sieve

    return (sieve,)


@app.cell
def _(sieve):
    def rotations(n: int) -> list[int]:
        nstr = str(n)

        return [
            int(nstr[i:] + nstr[:i])
            for i in range(len(nstr))
        ]

    N = 10**6 + 1
    primes = set(i for i in sieve.primerange(N))
    return primes, rotations


@app.cell
def _(primes, rotations):
    circular_primes = []

    for n in primes:
        if n > 10 and any(digit in str(n) for digit in "024568"):
            continue

        if all(rotation in primes for rotation in rotations(n)):
            circular_primes.append(n)
    return (circular_primes,)


@app.cell
def _(circular_primes):
    len(circular_primes)
    return


if __name__ == "__main__":
    app.run()
